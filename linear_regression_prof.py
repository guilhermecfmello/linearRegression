import matplotlib.pyplot as plt
import numpy as np

lim, npts = 10, 10

plt.xlim(-lim,lim)
plt.ylim(-lim,lim)
plt.grid()
pts = plt.ginput(npts)
plt.close()

pts = np.array(pts)

x = pts[:,0]
y = pts[:,1]

A = np.array([x,np.ones(len(x))]).T # Regressão linear
# A = np.array([x**2,x,np.ones(len(x))]).T # Regressão quadrática
# A = np.array([x**3,x**2,x,np.ones(len(x))]).T # Regressão cúbica

m = np.matmul(np.matmul(np.linalg.inv(np.matmul(A.T,A)),A.T),y)
print(m)

func = lambda XX: m[0]*XX + m[1] # Regressão linear
# func = lambda XX: m[0]*(XX**2) + m[1]*XX + m[2] # Regressão quadrática
# func = lambda XX: m[0]*(XX**3) + m[1]*XX**2 + m[2]*XX + m[3] # Regressão cúbica

X = np.linspace(-lim,lim,200)
Y = func(X)

plt.xlim(-lim,lim)
plt.ylim(-lim,lim)
plt.plot(x,y,"+")
plt.plot(X,Y)
plt.grid()
plt.show()