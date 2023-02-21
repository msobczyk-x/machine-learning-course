import numpy as np
import statistics
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

s = df['LICZBA']

#wartosc oczekiwana
mean = statistics.mean(s)

median = statistics.median(s)
mode = statistics.mode(s)

variance = statistics.pvariance(s)
standard_deviation = statistics.pstdev(s)

print("Średnia: ", mean)
print("Mediana: ", median)
print("Moda: ", mode)
print("Odchylenie standardowe: ", standard_deviation)
print("Wariancja: ", variance)

df.hist()


plt.show()