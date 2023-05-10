#!/usr/bin/env python3

import os
import subprocess

for path in sorted([path for path in os.listdir("test") if path.endswith(".rvg")], key=lambda s: int(s.split(".")[0])):
    print(f"starting {path}")
    subprocess.check_output(["rbu", "-b", "test.rbu", os.path.join("test", path)])
    subprocess.check_output(["riscv-compile.sh", "8", "ispm", os.path.join("src-gen", path.replace(".rvg", ".s"))])
    output = subprocess.run(["fp-emu"], stderr=subprocess.STDOUT, check=False, stdout=subprocess.PIPE).stdout.decode()
    output = output.split("    at Top.scala")[0]
    good_path = os.path.join("test/good/", os.path.basename(path).replace(".rvg", ".out"))
    if os.path.exists(good_path):
        with open(good_path, "r") as f:
            good = f.read()
        with open(good_path, "w") as f:
            f.write(output)
        if good != output:
            print(subprocess.check_output(["git", "diff", "--", good_path]).decode())
    else:
        os.makedirs(os.path.abspath(os.path.join(good_path, os.path.pardir)), exist_ok=True)
        with open(good_path, "a") as f:
            f.write(output)
    print(f" - {path} done")
