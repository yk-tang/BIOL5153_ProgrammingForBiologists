#! /usr/bin/bash

# This script generates a SLURM file for the AHPCC Pinnacle cluster

# define some variables
name = 'Trinity-assembly'
queue = 'comp06'
prefix = 'testpinnacle.$PBS_JOBID'
nodes = '--nodes=1' # number of nodes
proc = '--ntasks-per-node=32' # number of processors
wall = 6 # this is in hours

# This section prints the header/required info for the PBS script
print('#SBATCH -J', name) # job name
print('#SBATCH --partition', queue) # queue name
print('#SBATCH -o') # set the name of the job output file
print('#SBATCH -e')
print('#BATCHS --mail-type=ALL') 
print('#SBATCH --mail-user=yktang@uark.edu') 
print('#SBATCH', nodes) # how many resources to ask for (nodes = num nodes, ppn = num processors)
print('#SBATCH' proc)
print('#SBATCH --time'+ str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

print('export OMP_NUM_THREADS=32')
print()

# load the necessary modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
print()

# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')
print()

# copy files from storage to scratch
print ('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')
print()

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')
print()

# run the Trinity assembly
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')
print()

# copy output files back to storage
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')
print()