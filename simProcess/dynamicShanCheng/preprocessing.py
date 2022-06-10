import numpy as np 
import matplotlib.pyplot as plt

rhoL = 5.8
rhoG = 2.19
rad = 27.9
deltaP = 0.00274



# Unstable SKIRTED
Bo = 1.5e2
Mo = 1e3
viscRatio = 10.0

Bo = 1.5e2
Mo = 1e6
viscRatio = 10.0

cssq = 1.0/3.0
deltaRho = rhoL-rhoG
sigma = deltaP*rad 
d = rad*2.0

print('Sigma: ', sigma)
g = sigma*Bo/deltaRho/d**2
print('Gravity: ', g)

muL = np.sqrt(np.sqrt((sigma**3)*(rhoL**2)*Mo/(g*deltaRho)))
print('Mu L = ', muL)

kinL = muL/rhoL
print('kinL = ', kinL)

taoL = kinL/cssq+0.5
print('tao L = ', taoL)

muG = muL/viscRatio
print('muG = ', muG)

kinG = muG/rhoG
print('kinG = ', kinG)

taoG = kinG/cssq+0.5
print('taoG = ', taoG)

tn = np.sqrt(d/g)
print('tn = ', tn)

#Verification
print('Bo = ', g*deltaRho*d**2/sigma)
print('Mo = ', g*deltaRho*muL**4/sigma**3/rhoL**2)