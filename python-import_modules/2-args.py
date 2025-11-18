#!/usr/bin/python3
if __name__ == "__main__":
    import sys
args = sys.argv[1:]
a = len(args)
if a == 1:
    print("{} argument:".format(a))
elif a == 0:
    print("{} arguments.".format(a))
else:
    print("{} arguments:".format(a))
for i, arg in enumerate(args, 1):
    print("{}: {}".format(i, arg))
