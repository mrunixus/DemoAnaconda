# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:31:24 2016

@author: pedro.a.morales
"""

import pandas as pd

data = open('ds1.csv')

df = pd.DataFrame.from_csv(data,index_col=None)