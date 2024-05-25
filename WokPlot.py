import matplotlib.pyplot as plt
import control as ct
import numpy as np

# Definieren Sie Ihr System
s = ct.TransferFunction.s
t_1 = 15
t_2 = 1.4
k_1 = 1
k_2 = 1
strecke = 1/(s+1) 
regler = 1/s



ct.root_locus((regler * strecke))

plt.show()
