mkdir -p src-gen
rvgbuild
riscv-compile.sh 8 ispm src-gen/idot.s
fp-emu
