import sys

commandlineargs = sys.argv

with open("fil.txt") as data:
    for line in data:
        if line[0]=="H":
            species = line[:21].strip()
            when = line[21:37].strip()
            height = line[37:50].strip()
            mass = line[50:62].strip()
            brain = line[62:].strip()

with open("fil.txt", "w") as outfile:
    outfile.write("hei \n")
