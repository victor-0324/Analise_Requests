from mpl_toolkits import mplot3d 
import numpy 
import matplotlib.pyplot as plt 

x = numpy.outer(numpy.linspace(-2, 2, 10), numpy.ones(10)) 
y = x.copy().T
z = numpy.cos(x ** 2 + y ** 3) 
fig = plt.figure()
ax = plt.axes(projection ='3d') 
ax.plot_surface(x,y,z, cmap = 'viridis', edgecolor = 'green') 
ax.set_title('feito por vitor') 
plt.show()

