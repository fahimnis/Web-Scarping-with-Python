#!/usr/bin/env python
# coding: utf-8

# First we need to import the libraries that help us scrape webpages
# 

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


# Next we need to set our webpage of interest as an object

# In[477]:


url = 'https://www.worldometers.info/coronavirus/coronavirus-cases/'


# Then we request the content from the webpage and store it in a BeautifulSoup object 

# In[478]:


#Request content from webpage
result = requests.get(url)
c = result.content

#Set up BeautifulSoup object
soup = BeautifulSoup(c)


# The next step is to look at the source code of the website and identify the class which contains the data table. For this case it was in the  firt column was  inside class 'col-md-6' and the second inside 'table-responsive'. I used the find statement twice to extract each column.

# In[479]:


#Go to section of interest
summary1 = soup.find("div",{'class':'col-md-6',
                           'style':'margin-bottom:30px '})
summary2 = soup.find("div",{'class':'table-responsive',
                           'style':'font-size:16px; margin: auto; width:100%;'})
nums = soup.find_all("div",{'class':'number-table'})
table1 = summary1.find_all('table')
table2 = summary2.find_all('table')


# Now that we have the webpage contents we need to locate only the cells that contain text and numbers

# In[480]:


data1 = []
data2 = []
rows1 = table1[0].findAll('tr')
rows2 = table2[0].findAll('tr')

for tr in rows1:
    cols = tr.findAll('td')
    
    for td in cols:
        text = td.find(text=True)
#         print (text)
        data1.append(text)
        
        num = td.find()
#         print(num)
        data1.append(num)
        
        
for tr in rows2:
    cols2 = tr.findAll('td')
    
    for td in cols2:
        text = td.find(text=True)
#         print (text)
        data2.append(text)


# In[ ]:


data1


# In[ ]:


data2


# The lists contain some unnecesary elemetns. Let's clean up the lists so we only have the strings of interest.

# In[2]:


counthead1 = [0,4,8]
counthead2 = [0,2,4]
countval = [3,7,11]
countvals = [0,1,2,3,4,5]

headings1 = []
headings2 = []
headings = []
values = []

for i in counthead1:
    
    headings1.append(data1[i])
    
for i in counthead2:
    
    headings2.append(data2[i])
    
headings = headings1 + headings2
    
for i in countvals:
    for j in nums[i]:
        values.append(j)


# And put them together in a table for better presentation

# In[482]:


ValSer = Series(values,name = 'Numbers')#index = headings
NameSer = Series(headings,name = 'Category')
table = pd.concat([NameSer,ValSer],axis=1)


# In[483]:


table


# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# In[ ]:




