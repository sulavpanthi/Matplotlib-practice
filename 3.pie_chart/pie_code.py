import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
# plt.xkcd()

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode = [0.01, 0.01, 0.01, 0.1, 0.01]

plt.pie(slices, labels = labels, explode=explode, shadow=True, startangle = 90, autopct = '%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("First pie chart")
plt.tight_layout()
plt.savefig('plot.png')

plt.show()