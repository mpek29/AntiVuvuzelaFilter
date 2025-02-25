spectrum, freqs, line = plt.magnitude_spectrum(data, Fs=Fs, color='C1')
plt.xlim(0, 1700)
plt.ylim(35, 100)

#----------------------------------------------

plt.scatter(233, 92)

plt.scatter(2*233, 48)

plt.scatter(3*233, 70)

#plt.scatter(4*233,49)

plt.scatter(5*233,52)

plt.scatter(6*233, 48)

plt.scatter(7*233, 45)

print("Voici la liste des frequences (elles ont ete normalises pour etre des multiples de la fondamentale) :")
print(f"[233, {2*233}, {3*233}, {5*233}, {6*233}, {7*233}]")

print(f"L'abscence de la frequence {4*233}Hz est remarquable.")