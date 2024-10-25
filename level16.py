# Pengenalan Library dan Framework Populer di Python 
# Library untuk Data Manipulasi dan Analisis


#how to install pandas : pip3 install pandas

import pandas as pd
import numpy as np


data = {'Nama': ['Indra', 'Budi'], 'Umur': [35, 30]}
df = pd.DataFrame(data)
print(df)


array = np.array([1, 2, 3, 4])
print(array * 2)