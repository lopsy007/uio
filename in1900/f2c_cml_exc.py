import sys

try:
    temp = float(sys.argv[1])

except IndexError:
    print("Input a temp")
except ValueError:
    print("Input number as param 2")
