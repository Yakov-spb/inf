import sys
import numpy as np
s1 = pd.Series([5, 3, 2, 1, 4, 11, 13, 8, 7])
s2 = pd.Series([1, 5, 13, 2])
 
# вариант 1 (медленный)
ans1 = np.asarray([np.where(i == s1)[0].tolist()[0] for i in s2])
print(ans1)