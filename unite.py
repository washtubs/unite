#!/usr/bin/env python2
import globals
import getopt, sys, os
import os.path

def add_key():
    pass

def track():
    pass

def init():
    pass

def usage():
    print("Usage: \n\
    unite init \n\
    unite track [--relpath <path>] <file> \n\
    unite track -k <key> -k <key> <file> \n\
    unite track --diff <file> \n\
    unite add-key <key> \n")

def standard_args_check(opts):
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()

def file_is_trackable(f):
    pass


def main():
    private_keys_dir = os.getenv("UNITE_PRIVATE_KEYS",
            os.getenv("HOME",None) + "/" + ".ssh")
    unite_root = os.getenv("UNITE_ROOT",
            os.getenv("HOME",None) + "/" + ".unite")
    try:
        action = sys.argv[1]
        last = ""
        if action == "track" or action == "add-key": # expecting to use last element for this
            opts, args = getopt.getopt(sys.argv[2:-1], "hk:r:d", ["help", "key=", "relpath=", "diff" ])
            last = sys.argv[-1]
        else:
            opts, args = getopt.getopt(sys.argv[2:], "hk:r:d", ["help", "key=", "relpath=", "diff" ])
        print(args)
        print(opts)
        print(action)
        print(last)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    if action == "init":
        standard_args_check(opts)
    elif action == "track":
        standard_args_check(opts)
        fname = last
        print(fname)
        if os.path.isfile(fname):
            for o, a in opts:
                if o in ("-k", "--key"):
                    pass
                elif o in ("-r", "--relpath"):
                    pass
                elif o in ("-d", "--diff"):
                    pass
                else:
                    assert False, "unhandled option"
        else:
            assert False, "File " + fname + " does not exist."
    elif action == "add-key":
        standard_args_check(o, a)
        key = last


if __name__ == "__main__":
    main()
