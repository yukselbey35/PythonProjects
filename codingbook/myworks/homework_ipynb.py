#!/usr/bin/env python
# coding: utf-8

# Since you are closed up on your house for long days, you start to work out. At the beginning, you force yourself, but it ends up with you doing nothing. Then you start again. This time you plan your progress, and slowly increase your workout hours. The list given below named pushups is your first week results. Do the following tasks in order to analyze your data:
# 
# - Get input for the next day
# - Add it to the list
# - Find the day with most pushups
# - Find the day with least pushups
# - Find the average daily pushups
# - Pop last two days
# - Clear the list

# In[1]:


pushups = [30, 5, 0, 25, 50, 100]


# In[2]:


#Get input for the next day

nextDay=int(input("Enter the next day pushup: "))


# In[5]:


#Add it to the list
pushups.append(nextDay)
print(pushups)


# In[6]:


#Find the day with most pushups
maxPushUp=max(pushups)
print(f"My maximum pushup is:{maxPushUp}" )


# In[7]:


#Find the day with least pushups
leastPushUp=min(pushups)
print (f"My minimum push up is:{leastPushUp}")


# In[8]:


#Find the average daily pushups
totalDay=len(pushups)
sumPushUp=sum(pushups)
averagePushUps=(sumPushUp/totalDay)
print(f"The average daily pushup is:{averagePushUps}")


# In[9]:


#Pop last two days
pushups.pop(-1)
pushups.pop(-2)
print(pushups)


# In[11]:



#Clear the list
pushups.clear()
print(pushups)


# In[ ]:




