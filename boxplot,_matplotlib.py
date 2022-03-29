import matplotlib.pyplot as plt
v1=[72,76,24,40,57,62,75,78,31,32]
v2=[62,5,91,25,36,32,96,95,30,90]
v3=[23,89,12,78,72,89,25,69,68,86]
v4=[99,73,70,16,81,61,88,98,10,87]
box_plot_data=[v1,v2,v3,v4]
box=plt.boxplot(box_plot_data,vert=1,patch_artist=True,labels=['course1','course2','course3','course4'])
colors=['cyan','lightblue','lightgreen','tan']
for patch,color in zip(box['boxes'],colors):
    patch.set_facecolor(color)
plt.show()
