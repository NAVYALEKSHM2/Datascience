import matplotlib.pyplot as plt
ds=[5,15,25,35,45,55]
plt.hist(ds,bins=[0,12,20,30,40,50,60],weights=[20,10,45,33,6,8],histtype="bar",edgecolor="orange",color="green")
plt.show()