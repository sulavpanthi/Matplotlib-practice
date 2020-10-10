import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')

ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins = bins, edgecolor = 'black', log=True)

# for plotting a vertical line to denote median age
median_age = 29
color = '#ff3009'
plt.axvline(median_age, color=color, label='Median age', linewidth=2)
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

# adding extra xtick at the median age
plt.xticks(list(plt.xticks()[0]) + [29])
plt.tick_params(labelsize=10)

plt.tight_layout()

plt.savefig('plot.png')
plt.show()