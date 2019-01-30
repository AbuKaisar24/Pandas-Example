# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 22:04:09 2019

@author: dcL
"""

import pandas as pd 
import matplotlib.pyplot as plt
df=pd.DataFrame({"Day":[1,2,3,4],"Visitor":[100,200,300,400],"Bounce_rate":[20,45,60,10]})
df.set_index("Day",inplace=True)
df.plot()
plt.show()