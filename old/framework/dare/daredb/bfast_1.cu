#__author__    = "Sharath Maddineni"
#__copyright__ = "Copyright 2011-2012, Sharath Maddineni"
#__license__   = "MIT"


[echo_hello]
spmd_variation = single
number_of_processes = 1
multiple_args = True
arguments = arg_1,arg_2,arg_3,arg_4
out_arg_value = arg_4_key
arg_1_key = -a
#default value
arg_1_value = 123
arg_2_key = -b
arg_2_value = True
arg_3_key = -c 
arg_4_key = p
env_variables = env_1,env_2
env_1 = "PATH"

[machine_1]
executable = /path/to/bfast
arg_3_value = "/path/to/file"
env_1_value = "/usr/bin/"

[machine_2]
arg_3_value = "/path/to/file"
env_1_value = "/usr/bin/"
