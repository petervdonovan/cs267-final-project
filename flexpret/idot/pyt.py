#!/usr/bin/env python3

import os
import subprocess

for path in os.listdir("test"):
    if path.endswith(".rvg"):
        output = subprocess.check_output(["rbu", "-b", "test.rbu", "test/0.rvg"]).decode()
        output = subprocess.run(["fp-emu"], stderr=subprocess.STDOUT, check=False, stdout=subprocess.PIPE).stdout.decode()
        good_path = os.path.join("test/good/", os.path.basename(path))
        if os.path.exists(good_path):
            with open(good_path, "r") as f:
                good = f.read()
            with open(good_path, "w") as f:
                f.write(output)
            if good != output:
                print(subprocess.check_output(["git", "diff", "--", good_path]).decode())
        else:
            os.makedirs(os.path.abspath(os.path.join(good_path, os.path.pardir)))
            with open(good_path, "a") as f:
                f.write(output)
