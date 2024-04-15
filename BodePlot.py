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
k_s = 100
t_s1 = 100
t_s2 = 5
t_s3 = 1
strecke = k_s/((1+s*t_s3)*(1+t_s1*s)*(1+t_s2*s))

# Definieren Sie die Übertragungsfunktion des Reglers
k_r_db = -60
k_r = 10**(k_r_db/20) 
t_r1 = t_s1
regler = k_r * (1+t_r1*s) / s
print(k_r)

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

# Draw a line at -120 degrees in the phase diagram
plt.axhline(y=-120, color='r', linestyle='--')
# Zeigen Sie das Diagramm an
plt.show()