from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('TkAgg')


actual = numpy.random.binomial(1, .9, size=1000)
predicted = numpy.random.binomial(1, .9, size=1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix, display_labels=[False, True])

cm_display.plot()
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
