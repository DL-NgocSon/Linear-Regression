import numpy as np
import matplotlib.pyplot as plt

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
y = np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

plt.plot(X, y, 'ro')
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

print(X.shape[0])
ones = np.ones((X.shape[0]))
X_bar = np.concatenate((ones, X), axis = 1)
A = np.dot(X_bar.T, X_bar)
b = np.dot(X_bar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)

w_0 = w[0][0]
w_1 = w[1][0]
x_0 = np.linspace(145, 185, 2)
y_0 = w_0 + w_1*x_0

plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()