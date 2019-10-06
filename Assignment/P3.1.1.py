import math
import pylab
import numpy as np

ax = pylab.linspace(-20, 20, 1001)
cosine = np.cos(ax)
sine = np.sin(ax)
ay = pylab.log(1/(cosine)**2)
by = pylab.log(1/sine**2)

pylab.plot(ax,ay,ax,by)
pylab.show()


n = pylab.linspace(-20, 20, 1001)
cosine = np.cos(n*math.pi/2)
sine = np.sin(n*math.pi/2)
ay = pylab.log(1/(cosine)**2)
by = pylab.log(1/sine**2)

pylab.plot(ax,ay,ax,by)
pylab.show()