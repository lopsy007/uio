import matplotlib.pyplot as plt

# Finner baseline aksellerasjon
with open("fys1100/heis_forsok/ro.csv") as d:
    # Formattering
    lines = [line.strip() for line in d]
    lines.pop(0)
    lines = [line.split(",") for line in lines]
    data = list(zip(*lines))
    a_z = list(map(float,data[3]))

    # Finner snittet
    average = sum(a_z)/len(a_z)
    print(average)

# Plotter aksellerasjon
with open("fys1100/heis_forsok/heis.csv") as d:
    lines = [line.strip() for line in d]

    #Formattering
    lines.pop(0)
    lines = [line.split(",") for line in lines]
    data = list(zip(*lines))
    time = list(map(float,data[0]))
    a_z = list(map(float,data[3]))
    average = sum(a_z)/len(a_z)-0.0035
    a_z_kalibrert = [a-average+9.81 for a in a_z]


    plt.show()

v = [0.0]
s = [0.0]
for i in range(1, len(a_z_kalibrert)):
    v.append(v[i-1]+(a_z_kalibrert[i]-9.81)*(time[i]-time[i-1]))
    s.append(s[i-1]+v[i]*(time[i]-time[i-1]))

#Plotting
plt.plot(time, a_z)
plt.plot(time, a_z_kalibrert)
plt.plot(time, [sum(a_z_kalibrert)/len(a_z_kalibrert) for _ in a_z_kalibrert])
plt.show()
plt.plot(time, v)
plt.plot(time, s)
plt.show()
