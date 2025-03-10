def compute_component(f0,C1,R4,df):
    m=df/(2*f0)
    R1 = 1/(2*np.pi*C1*f0)
    R2 = R1
    R3=R1/2
    C3=2*C1
    Q = 1/(2*m)
    R5=R4*(4*Q-1)
    return {"C1":"{:.2e}".format(C1),"C2":"{:.2e}".format(C1), "R1":"{:.2e}".format(R1), "R2":"{:.2e}".format(R1), "R3":"{:.2e}".format(R3), "R4":"{:.2e}".format(R4), "R5":"{:.2e}".format(R5)}
    

# example
C1=1*(10**-9)
R4=1*(10**3)
freqs= [
    {"f0": 233, "df": 100},
    {"f0": 466, "df": 250},
    {"f0": 699, "df": 175},
    {"f0": 1165, "df": 290},
    {"f0": 1398, "df": 250},
    {"f0": 1631, "df": 300},
]

for freq in freqs:
    print(compute_component(freq["f0"],C1,R4,freq["df"]))
    
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '6.83e+05', 'R2': '6.83e+05', 'R3': '3.42e+05', 'R4': '1.00e+03', 'R5': '8.32e+03'}
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '3.42e+05', 'R2': '3.42e+05', 'R3': '1.71e+05', 'R4': '1.00e+03', 'R5': '6.46e+03'}
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '2.28e+05', 'R2': '2.28e+05', 'R3': '1.14e+05', 'R4': '1.00e+03', 'R5': '1.50e+04'}
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '1.37e+05', 'R2': '1.37e+05', 'R3': '6.83e+04', 'R4': '1.00e+03', 'R5': '1.51e+04'}
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '1.14e+05', 'R2': '1.14e+05', 'R3': '5.69e+04', 'R4': '1.00e+03', 'R5': '2.14e+04'}
# {'C1': '1.00e-09', 'C2': '1.00e-09', 'R1': '9.76e+04', 'R2': '9.76e+04', 'R3': '4.88e+04', 'R4': '1.00e+03', 'R5': '2.07e+04'}