"""This module demonstrates passing variable length of arguments through command
line."""
import sys

def print_args(argv):
    '''Print command line args.'''
    print("Total number of args: ", len(argv))
    for arg in range(0, len(argv)):
        print("arg%d : %s" % (arg, argv[arg]))

if __name__ == '__main__':
    print_args(sys.argv)

#pylint: disable=pointless-string-statement
"""*********** OUTPUT *************
$ python practise/var_len_args.py a b c d e f g h i j k
Total number of args:  12
arg0 : practise/var_len_args.py
arg1 : a
arg2 : b
arg3 : c
arg4 : d
arg5 : e
arg6 : f
arg7 : g
arg8 : h
arg9 : i
arg10 : j
arg11 : k
"""
