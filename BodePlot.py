import matplotlib.pyplot as plt
import control as ct
import numpy as np

s = ct.TransferFunction.s

# Definition vom Diagramm:
title = 'Bode-Diagramm'

# Definietion von Omega Start und Omega Stop:
omega_start = 0.001
omega_stop = 10000
omega_steps = 1000

# Definieren Sie die Übertragungsfunktion der Strecke
k_mech = 5.21
k_el = 6.25*10**-2
k_s = k_mech*k_el
k_r_db = 20
k_r = -10**(k_r_db/20) 
print(f"Verstärkung Regler: {k_r}")

t_mech = 2.266*10**-2
t_el = 5*10**-4
t_v = t_mech
t_d = 0.05*t_v

strecke = k_s/((1+s*t_el)*(1+t_mech*s)*(1-t_mech*s))
regler = (k_r * (1+t_v*s)) / (1+t_d*s)

# System = Regler * Strecke
system = regler * strecke

# Create omega
omega = np.logspace(start=(np.log10(omega_start)),
                    stop=(np.log10(omega_stop)),
                    num=omega_steps)

# Erstellen Sie das Bode-Diagramm
mag, phase = ct.bode(system,
                     omega=omega,
                     dB=True,
                     deg=True,
                     Hz=False,
                     title=title)

# Draw a line at -180 degrees in the phase diagram
#plt.axhline(y=-180, color='r', linestyle='--')
# Zeigen Sie das Diagramm an
plt.show()