import matplotlib.pyplot as plt
import numpy as np

limmin = 4000.
limmax = 7000.
waverange = 60.
level = 18. #18 es sodio doublet pag(71), 7 Halpha (),  
n = 49. - level  # from 0 to 49

wavemin = limmin + waverange * n
wavemax = limmin + waverange * (n+1.)

#wavemin = 658.
#wavemax = 652.

list = open('all400to700nm.txt').readlines()
wave = [i.split()[0] for i in list] 
flux = [ (462020*float(i.split()[2]))/3.14159  for i in list]
wave2 = np.array(wave, dtype='float') * 10.
flux2 = np.array(flux, dtype='float')
uniquewave = np.unique(wave2, return_index=True)
waveu = uniquewave[0]
fluxu = flux2[uniquewave[1]]
plt.plot(waveu, fluxu)
#plt.xlim(wavemin,wavemax)
plt.xlim(wavemax,wavemin)
plt.show()


