# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 01:13:43 2025

@author: HP
"""

from sklearn import SimpleImputer
import numpy as np

data=np.array([
    [1, 2, np.nan],
    [4, np.nan, 6],
    [np.nan, 8 , 9]
])

imputer = SimpleImputer(Strategy="mean")

imputed_data = imputer.fit_transform(data)

data

imputed_data