import numpy as np 
import matplotlib.pyplot as plt

cssq = 1.0/3.0
rhoL = 7.7
rhoG = 0.5
d = 40.0
rad = d/2.0
viscRatio = 10.0
deltaRho = rhoL-rhoG
deltaP = 8.5e-3-5.87e-3
sigma = deltaP*rad 
Bo = 10.0
Mo = 2e-2

print('Sigma: ', sigma)
g = sigma*Bo/deltaRho/d**2
print('Gravity: ', g)

muL = np.sqrt(np.sqrt(sigma**3*rhoL**2*Mo/(g*deltaRho)))
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

taoL2 = 2.0
kinL2 = cssq*(taoL2-0.5)
muL2 = kinL2*rhoL
Mo2 = g*deltaRho*muL2**4/(sigma**3*rhoL**2)
print('muL, Mo2 = ', muL2, Mo2)

#Verification
print('Bo = ', g*deltaRho*d**2/sigma)
print('Mo = ', g*deltaRho*muL**4/sigma**3/rhoL**2)