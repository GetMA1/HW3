# -*- coding: utf-8 -*-
"""Greg_Louis HW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OfPLlPrL0NX7o04oJYaliHyyEWV5HlcU

**Q1**. Please read WorldCupMatches.csv to a data frame to proceed
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import csv

df = pd.read_csv('/content/drive/MyDrive/DATA/WorldCupMatches.csv')

"""**Q2** Using seaborn's displot draw density curves to show the distributions of Home Team Goals for every year. """

sns.displot(df["Home Team Goals"], kind='kde')

"""**Q3** Draw violin plots to summarize Home Team Goals distributions for each year by using seaborn. Notice that labels are really clutterd. Then please refer to the earlier notebooks to have labels to appear on only select years which end with 0. You can use ax handle to call ax.set_xticklables(labels) for the labels your prepared."""

labels=[y if y%5==0 else None for y in list(df.Year.unique())]

ax = sns.violinplot(data=df, x='Year', y='Home Team Goals')
ax.set_xticklabels(labels)

"""**Q4** Please install joypy. Then visualize distributions for Home Team Goals and Away Team Goals' for each year. Once you visualize, please add  plt.style.use('seaborn-white') to see how colors change in your second run. Please also add the legend which you can find from the function prototype.


"""

!pip install joypy

import joypy as jp
from matplotlib import cm
print(plt.style.available)
plt.style.use('seaborn-white')
jp.joyplot(data=df, column=['Home Team Goals', 'Away Team Goals'], by='Year', legend='true' )
#plt.style.use('seaborn-white')

"""**Q5** Please use groupby function on Home Team Initials to see the sum of Home Team Goals which can be saved to another data frame by adding .reset_index() end the end of your line. 

Then use your new data frame to visualize those total Home Team Goals for your top 5 countries (You can use Home Team Initials). You can use use df.sort_values() function on your data frame by tweaking the ascending option.

Notice that your x-axis will be having country initials, and y-axis will show the total number of Home Team Goals. 


"""

df.groupby(['Home Team Goals']).sum()

df.reset_index()

df.sort_values(by='Home Team Goals', ascending=False)

"""**Q6** Please extract the rows for your top 4 countries (Home Team Initials') with the help of the previous question's answer. Then use joyplot again to visualize densities for 'Home Team Goals' and	'Away Team Goals' on the horizantal axis. Notice that your y-axis labels will be your country initials (Home Team Initials'). Make sure that your legend is visible and use 'dark_background' by calling plt.style.use again.


"""

import joypy as jp
from matplotlib import cm
print(plt.style.available)
plt.style.use('dark_background')
jp.joyplot(data=df, column=['Home Team Goals', 'Away Team Goals'], by='Year', legend='true' )

"""**Q7** Please install seaborn_qqplot as shown below. Then draw a qqplot to compare probability distributions of Home Team Goals and Away Team Goals. Please comment on your finding. Do you think their distributions agree with each other? Please justify your answer by explaining the figure you obtained."""

!pip install seaborn_qqplot

from seaborn_qqplot import pplot #seaborn-qqplot is a seaborn extension adding qqplots.
plt.style.use('ggplot') #this is to change the color theme. 
from scipy.stats import norm
pplot(df, x='Home Team Goals', y='Away Team Goals', kind = 'qq', display_kws={"identity":True}, height=4, aspect=2)
#pplot(df, x='Home Team Goals', y=norm, kind = 'qq', display_kws={"identity":True}, height=4, aspect=2)

"""No. According to the graph it shows that the team scored more goals at home than away. """