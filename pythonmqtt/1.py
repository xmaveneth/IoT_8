import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# График температуры
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['temperature'], marker='o', linestyle='-', color='b')
plt.xlabel('Время')
plt.ylabel('Температура')
plt.title('График температуры')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# График движения
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['motion'], marker='o', linestyle='-', color='g')
plt.xlabel('Время')
plt.ylabel('Движение')
plt.title('График движения')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# График напряжения
plt.figure(figsize=(10, 6))
plt.plot(data['time'], data['power'], marker='o', linestyle='-', color='r')
plt.xlabel('Время')
plt.ylabel('Напряжение')
plt.title('График напряжения')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

