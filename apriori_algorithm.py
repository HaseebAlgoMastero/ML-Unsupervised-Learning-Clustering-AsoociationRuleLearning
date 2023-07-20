# -*- coding: utf-8 -*-
"""Apriori Algorithm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1reBJNoHBsENvilBGyGs7zDrVEa2BymhJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

!pip install apyori

df = pd.read_csv('Market_Basket_Optimisation.csv',header = None)

df.shape

transactions =[]
for i in range(0,7501):
  transactions.append([str(df.values[i,j]) for j in range(0,20)])
print(transactions)

from apyori import apriori
rules  = apriori(transactions = transactions,min_support = 0.003, min_confidence = 0.4, min_lift = 4,min_length = 2,max_length = 4)

# rules = list(rules)
rules