#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define some variables
name = 'testrazor' # job name
queue = 'med16core'
prefix = 'testrazor.$PBS_JOBID'
nodes = 'nodes=1' # number of nodes
proc = 'ppn=1' # number of processors
wall = 3 # this is in hours

# This section prints the header/required info for the PBS script
print('#PBS -N', name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o', prefix) # set the name of the job output file
print('#PBS -l', nodes + ':' + proc) # how many resources to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')