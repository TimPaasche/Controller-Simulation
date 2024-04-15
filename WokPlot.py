import matplotlib.pyplot as plt
import control as ct

# Definieren Sie Ihr System
s = ct.TransferFunction.s
t_1 = 1
t_2 = 0.1
strecke = 1/(s*(1+t_1*s)*(1+t_2*s))

# Wurzelortskurve plotten
rlocus = ct.root_locus(strecke)

plt.show()