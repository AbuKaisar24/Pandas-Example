# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:31:57 2019

@author: dcL
"""

import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("new.csv")
print(data)
data.plot()
plt.show()