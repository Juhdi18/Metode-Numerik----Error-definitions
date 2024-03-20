import math as mt
import numpy as np
import matplotlib.pyplot as plt

n = 3
x = 0.5
eksak = mt.e**x
tollapprox = (0.5 * 10 **(2-n))
epsT = np.zeros(25, dtype=float)
epsA = np.zeros(25, dtype=float)
hasil = np.zeros(25, dtype=float)

for i in range(25):
    hasil[i] = (x**i)/mt.factorial(i) + hasil[i-1] if i != 0 else (x**i)/mt.factorial(i)
    epsT[i] = abs((eksak - hasil[i]) / eksak)*100 
    epsA[i] = abs((hasil[i] - hasil[i-1]) / hasil[i])*100 if i != 0 else 0
    if i > 1 and epsA[i] < tollapprox:
        break
    print("Term:", i+1)
    print("Hasil perkiraan:", hasil[i])
    print("Epsilon t:", epsT[i])
    print("Epsilon a:", epsA[i])
    print("--------------------")

# Plotting the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(range(i+1), hasil[:i+1], marker='o', color='b')
plt.xlabel('Iteration')
plt.ylabel('Estimated Value')
plt.title('Estimated Value vs Iteration')

plt.subplot(1, 3, 2)
plt.plot(range(i+1), epsA[:i+1], marker='o', color='r')
plt.xlabel('Iteration')
plt.ylabel('Epsilon a (%)')
plt.title('Epsilon a vs Iteration')

plt.subplot(1, 3, 3)
plt.plot(range(i+1), epsT[:i+1], marker='o', color='g')
plt.xlabel('Iteration')
plt.ylabel('Epsilon t (%)')
plt.title('Epsilon t vs Iteration')

plt.tight_layout()
plt.show()
