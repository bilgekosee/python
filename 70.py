# AUC-ROC EĞRİSİ
# Sınıflandırmada biçok farklı değerlendirme ölçütü vardır. En popüler olanı
# modelin ne sıklıkla doğru olduğunu ölçen doğrı-uluktur.bu harika bir ölçüm çünkü anlaşılması  kolay
# ve çoğu zaman en doğru tahminlerielde etmek isteniyor.

# diğer bir yaygın ölçüm alıcı işletim karakteristiği (ROC) eğrisinin altında kalan AUC dir.
# alıcı işletim karakteristik eğrisi arklı sınıflandırma eşiklerinde gerçek pozitif (TP)
# oranı ile yanlış pozitif FP oranını gösterir.

# Verilerimizin çoğunluğunun tek bir değere sahip olduğu dengesiz bir veri setimiz olduğunu varsayalım. Çoğunluk sınıfını tahmin ederek model için yüksek doğruluk elde edebiliriz.

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
n = 10000
ratio = .95
n_0 = int((1-ratio)*n)
n_1 = int(ratio*n)

y = np.array([0]*n_0 + [1] * n_1)

y_proba = np.array([1]*n)
y_pred = y_proba > .5

print(f'accuracy score:{accuracy_score(y,y_pred)}')
cf_mat = confusion_matrix(y, y_pred)
print('Confusion matrix')
print(cf_mat)
print(f'class 0 accuracy: {cf_mat[0][0]/n_0}')
print(f'class 1 accuracy: {cf_mat[1][1]/n_1}')
