# Pyplot ile, x ve y ekseni için bir etiket ayarlamak üzere xlabel()ve işlevlerini kullanabilirsiniz . ylabel()
# title()Pyplot ile arsa için bir başlık ayarlamak üzere işlevi kullanabilirsiniz .
# Başlık ve etiketlerin yazı tipi özelliklerini ayarlamak için , ve fontdictiçindeki parametreyi kullanabilirsiniz .xlabel()ylabel()title()
# grid()Pyplot ile, grafiğe ızgara çizgileri eklemek için işlevi kullanabilirsiniz .
# Izgaranın çizgi özelliklerini de şu şekilde ayarlayabilirsiniz: grid(color = ' color ', linestyle = ' linestyle ', linewith = number ).


import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title("sports data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()

# Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
