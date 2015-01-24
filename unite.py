#!/usr/bin/env python2
import globals
import getopt, sys, os

def usage():
    print("Usage: \n\
    unite init \n\
    unite track [--relpath <path>] <file> \n\
    unite track -k <key> -k <key> <file> \n\
    unite track --diff <file> \n\
    unite add-key <key> \n")

def main():
    unite_root = os.getenv("UNITE_ROOT",
            os.getenv("HOME",None) + "/" + ".unite")
    try:
        action = sys.argv[1]
        opts, args = getopt.getopt(sys.argv[2:], "hk:r:d", ["help", "key=", "relpath=", "diff" ])
        last = sys.argv[-1]
        print(args)
        print(opts)
        print(action)
        print(last)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err)) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    main()
