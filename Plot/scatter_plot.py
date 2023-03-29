import matplotlib.pyplot as plt

data = {
    "x" : [i for i in range (1,15)],
    "y" : [i * i for i in range (1,15)]
    }
plt.scatter(
    data["x"],
    data["y"],
    marker="o"
    )
plt.show()