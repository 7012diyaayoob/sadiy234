#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Reab dataset
# 

# In[4]:


df


# In[7]:


#Change data in column height with random numbers between 150 180
height_data=np.random.randint(150,181,size=len(df))
df['Height']=height_data
df


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.info()


# In[11]:


df.describe(include='all')


# In[12]:


df.isnull().sum # To check if ther are any missing values


# In[13]:


df.duplicated().sum()# To count number of duplicate rows


# In[14]:


df.columns # view columu names


#     How many are there in each team and the percentage splitting with respect
#     to the total employees.

# In[15]:


team_count=df['Team'].value_counts()
total_count=len(df)
percentage=(team_count/total_count)*100
result=pd.DataFrame({"Number of employees":team_count,'percentage splitting':percentage})
print(result)


# 2.Segregate the employees W.r.t different positions.

# In[16]:


df['Position'].value_counts()


# 3 Find from which age group most of the employees belong to.

# In[17]:


age_count=df['Age'].value_counts()
print("Age group most employees belong to:",age_count.idxmax())
print("Number of employees:",age_count.max())


# 4.Find out under which team and position,spending in terms of salary is high.

# In[18]:


highest_salary=df['Salary'].idxmax()
hs=df.loc[highest_salary,['Team','Position']]
print("Highest Salary:",df['Salary'].max())
print(hs)


# 5.Find if there is anny correlation between age and salary,represent it visually

# In[19]:


corr=df[['Age','Salary']].corr()
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Correlation between age and salary')
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()


# In[20]:


plt.xlabel('Age')
('Salary')
plt.title('Correlation between age and salary')
sns.scatterplot(x='Age',y='Salary',data=df)
plt.show()


# In[ ]:




