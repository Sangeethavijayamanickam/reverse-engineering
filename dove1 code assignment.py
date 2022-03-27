# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:07:26 2022

@author: Dell
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dove = pd.read_excel("C:/Users/Dell/Documents/imarticus/dove sample1.xlsx")
dove.head()
dove.size
dove.shape
dove.tail()
dove.count()
plt.boxplot(dove.women,dove.men)
dove.women.hist()
dove.men.hist()
dove.women.describe()
women = [25,24,26,26,28,24,23,22,27]
men =   [19,21,23,24,28,23,23,24,20]
plt.bar(women,men,color='red')
plt.barh(women,men)
plt.pie(women)
plt.scatter(women,men)
plt.figure(figsize=(14,18))
plt.scatter(women,men)
plt.plot(x,y)
plt.xlabel('women')
plt.ylabel('years')
plt.title("dove")
plt.grid()
