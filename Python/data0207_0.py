import numpy as np
import pandas as pd

s1 = pd.Series([100,200,300,np.nan], index = ["사과", "배", "한라봉", "천혜향"])
# print(s1)

s2 = pd.Series([100,200,300,500], index = ["사과", "한라봉", "천혜향", "무화과"])
# print(s2)

print(s1+s2)
