import sys

print("sys.argv = ", sys.argv)
print("len(sys.argv) =", len(sys.argv))

if len(sys.argv) > 1:
    print("Arguments after script name:", sys.argv[1:])
else:
    print("No additional arguments.")
