with open("f2c_file_read_data.txt") as file:
    lines = file.readlines()
    words = lines[3].split()
    print(words[2])
