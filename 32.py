import matplotlib.pyplot as plt
import numpy
import matplotlib
import sys
matplotlib.use('TkAgg')

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
