# Diyelim ki bu sefer üç rengimiz var, kırmızı, mavi ve yeşil.
#  İlk sütunu düşürürken get_dummies yaptığımızda aşağıdaki tabloyu elde ederiz.

import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']
print(dummies)
