import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

bins = [20, 25, 30, 35, 40, 45, 50, 55, 60]

plt.hist(ages, bins=bins, edgecolor='black')
plt.title('Age distribution')
plt.xlabel('Ages')
plt.ylabel('Number of people')
plt.tight_layout()

plt.savefig('plot.png')
plt.show()