# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 21:53:28 2019

@author: dcL
"""

import pandas as pd 
df1 =pd.DataFrame({"HPI":[80,90,60,70],"Int_rate":[2,1,2,3,],"IND_GDP":[50,45,60,35]},
                   index=[2001,2002,2003,2004])
df2 =pd.DataFrame({"Low":[800,900,600,700],"Unemployment":[20,10,20,30]},
                   index=[2005,2006,2007,2008])
join=df1.join(df2)
print(join)
