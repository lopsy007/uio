with open("f2c_file_read_write_data.txt") as file:
    lines = file.readlines()
    del lines[:3]
    temps = [float(line.split()[2]) for line in lines]

with open("f2c_file_read_write_output.txt", "w") as file:
    file.writelines(str(temps))
