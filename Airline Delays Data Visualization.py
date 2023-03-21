#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import networkx as nx
import matplotlib.dates as md
import matplotlib.font_manager as fm
import matplotlib.gridspec as gridspec
import warnings; warnings.filterwarnings("ignore")


# In[2]:


#Reading CSV and creating tables
flight_data = pd.read_csv("Desktop/flight_delays.csv", index_col="Month")

flight_data.head()


# In[3]:


#Creating bar graph for Spirit Airlines delayed flights
##Setting graph parameters
plt.figure(figsize=(10,6))
##Adding title
plt.title("Average Delays for Spirit Airlines on a Monthly Basis")
##plotting graph
sns.barplot(x=flight_data.index, y=flight_data["NK"])
##Adding label to vertical axis
plt.ylabel("Arrival delay (in minutes)")


# In[4]:


#Creating a heatmap
##Setting parameters
plt.figure(figsize=(14,7))
##title
plt.title("Average Arrival Per Airline on a Monthly Basis")
##Heatmap
sns.heatmap(data=flight_data, annot=True)
##Label for horizontal axis
plt.xlabel("Airline")


# In[8]:


#Spirit Airlines Delays Scatter plot
sns.scatterplot(x=flight_data.index, y=flight_data["NK"])


# In[9]:


#Spirit Airlines Delays Scatter plot with regression line
sns.regplot(x=flight_data.index, y=flight_data["NK"])


# In[10]:


#Density Plot
sns.kdeplot(data=flight_data, shade=True)


# In[11]:


#2D Density Plot for Spirit Airlines Delays
sns.jointplot(x=flight_data.index, y=flight_data["NK"], kind="kde")


# In[13]:


#Lineplot of Airline delays per month
sns.lineplot(data=flight_data)


# In[ ]:




