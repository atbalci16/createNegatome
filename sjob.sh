#!/bin/bash
#BATCH -J NegatomeDecoys
#SBATCH -p longer
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --output=create_negatome_structure.out

OLD_PATH=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH="$(pwd)/libg2c":$LD_LIBRARY_PATH
python extract_chains.py pair_list.txt proteins chains
python create_dock.py pair_list.txt chains docks preprocessed
LD_LIBRARY_PATH=$OLD_PATH
exit 0
