import matplotlib.pyplot as plt

labels = ["east", "south", "north", "west"]
sizes = [5, 10, 20, 15]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.1, 0)

plt.pie(sizes, explode = explode, labels = labels, colors = colors,  labeldistance=1.2, autopct="%3.1f%%", shadow=True, startangle=0, pctdistance=0.6)
plt.axis("equal")
plt.legend()
plt.show()