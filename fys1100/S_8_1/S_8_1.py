import matplotlib.pyplot as plt

with open("S_8_1.txt") as file:
    file.readline()
    y,t = zip(*[tuple(map(float,line.strip().split(", "))) for line in file.readlines()]) #[[2,0], [...], ...]

print(y,t)


v = tuple((y[i+1]-y[i])/(t[i+1]-t[i]) for i in range(len(y)-1))


# Tror akselerasjon kommer til å først være nær 9.81 ved t=0 og så gå mot null, og etter omtrent t=0.26 være konstant lik null

a = tuple((v[i+1]-v[i])/(t[i+1]-t[i]) for i in range(len(v)-1))
plt.plot(t,y)
plt.plot(t[:-1],v)
plt.plot(t[:-2],a)
plt.show()

# a blir null omtrent ved t=0.4s. Man kan også se det på v- og y -grafene, henholdsvis når farten blir konstant og posisjonen blir lineær, men det vil skje tidligere for v og ennå tidligere for y, siden den totale endringen (integralet) er veldig lite når tidssteget er kort (t omtrent lik 0.3)