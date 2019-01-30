# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:07:54 2019

@author: dcL
"""
import pandas as pd
web={'Day':[1,2,3,4,5],'Visitor':[100,2000,300,500,600],'Rate':[10,100,3,5,6]}
df=pd.DataFrame(web)
print(df)
print(df.head(2))
print(df.tail(2))
