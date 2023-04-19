mkdir -p src-gen
rbu &&
riscv-compile.sh 8 ispm src-gen/idot.s &&
fp-emu
