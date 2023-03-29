import matplotlib.pyplot as plt

data1= {
    "x" : [i for i in range (1,10)],
    "y" : [i * i for i in range (1,10)]
    }
data2={
    "x" : [i for i in range (1,10)],
    "y" : [i * 10 for i in range (1,10)]
    }
plt.plot(
    data1["x"],
    data1["y"],
    color="g"
    )
    
plt.scatter(
    data2["x"],
    data2["y"],
    marker="o"
    )
plt.xlabel("v")
plt.title("V-T Graph", fontsize=20,color='c')
plt.ylabel("t")
plt.show()