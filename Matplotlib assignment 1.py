#!/usr/bin/env python
# coding: utf-8

# Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
# Matplotlib.

# # Matplotlib is a python library used to create 2D graphs and plots by using python scripts.
# Matplotlib is extremely powerful because it allows users to create numerous and diverse plot types.
# 1.plot
# 2.bar graph
# 3.Scatter
# 4.Line
# 5.Histogram

# Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.
# import numpy as np
# np.random.seed(3)
# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))
# Note: Also add title, xlabel, and ylabel to the plot.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))


# Q2: What is a scatter plot?

# Scatter plots are the graphs that present the relationship between two variables in a data-set

# In[2]:


x


# In[3]:


y


# In[5]:


plt.scatter(x,y)
plt.title("This is scatter")
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")

Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
Use the following data:
import numpy as np
For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])
# In[7]:


#For line 1
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 100, 200, 300, 400, 500])


# In[8]:


x


# In[9]:


y


# In[38]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 100, 200, 300, 400, 500])
plt.subplot(221)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([50, 20, 40, 20, 60, 70])

plt.subplot(222)
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(223)
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(224)
plt.plot(x,y)


plt.show()

Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
# Q4: What is a bar plot? Why is it used?

# The bar plot is another univariate plot on a two-dimensional axis. The two axes are not called x- or y-axes. Instead, one axis is called the category axis showing the category name, while the other, the value axis, shows the numeric value of that category, given by the length of the bar.

# In[42]:


#Using the following data plot a bar plot and a horizontal bar plot.
import matplotlib.pylab as plt
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])


# In[46]:


plt.bar(company,profit)
plt.xlabel("Company's Name")
plt.ylabel("Company's profit")
plt.title("Bar Graph")


# In[47]:


import matplotlib.pylab as plt
import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.barh(company,profit)
plt.xlabel("Company's Name")
plt.ylabel("Company's profit")
plt.title("Bar Graph")


# 

# 

# In[49]:





# In[50]:





# In[52]:





# In[ ]:




