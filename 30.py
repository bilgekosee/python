# pasta grafiği oluşturmak için pie()
# label her dilim için etiket oluşturur
# dilimlerden birinin öne çıkmasını explode ile sağlayabilirsiniz
# shadow parametresi ile grafiğe gölge ekleyebilirsiniz.
# colors parametresi ile renk ayarlayabilirsin
# her dilime açıklma eklme için legend() kullanılır açıklamaya başlık eklemek için legende title eklenebilir

import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib
matplotlib.use('TkAgg')

y = np.array([30, 15, 42, 21])
mylabels = ["mercedes", "audi", "ferrari", "bmw"]
myexplode = [0, 0, 0.2, 0]
mycolors = ["black", "darkblue", "red", "purple"]
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="best cars")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
