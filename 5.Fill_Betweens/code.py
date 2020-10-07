import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')

age_data = data['Age']
all_devs_data = data['All_Devs']
py_devs_data = data['Python']

plt.plot(age_data, all_devs_data, color = '#444444', linestyle = '--', label = 'All Devs')
plt.plot(age_data, py_devs_data, label = 'Python')

plt.fill_between(age_data, py_devs_data, all_devs_data, where=(py_devs_data>all_devs_data),interpolate = True, alpha=0.25, label='Above avg')

plt.fill_between(age_data, py_devs_data, all_devs_data, where=(py_devs_data<all_devs_data),interpolate = True, alpha=0.25, label='Below avg', color='red')

plt.legend()
plt.title('Median salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median salary (USD)')
plt.tight_layout()
plt.savefig('plot.png')
plt.show()

