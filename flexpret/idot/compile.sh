unset VERILATOR_ROOT
export VERILATOR_ROOT=/home/peter/school/267/verilator
export PATH=/home/peter/school/267/verilator/bin:$PATH
export JAVA_OPTS="-Xms4G -Xmx8G"
make emulator N_CORES=16 THREADS=8
