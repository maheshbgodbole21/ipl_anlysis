#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #Importing the data for analysis from matches.csv

# In[14]:


data= pd.read_csv('matches.csv')


# #verifying the columns availble in the data

# In[15]:


data.columns


# #checking the top two rows availble in the data

# In[16]:


data.head(2)


# In[ ]:





# # pre processing the data required for analysis

# Removing the non required feilds from the data

# In[17]:


data=data.drop(['umpire1','umpire2','umpire3'],axis=1)


# In[18]:


data.head(2)


# #Removing the null value if any

# In[19]:


data.shape


# In[20]:


data =data.dropna(how='all')


# In[21]:


data.shape  #there are no rows where all element are null


# checking  the types of data avaible 

# In[22]:


data.info()


# #converting date type from object to datetime

# In[23]:


data['date']= pd.to_datetime(data['date']) 


# In[24]:


data.info()


# #create the backup of the data

# In[25]:


df = data


# In[26]:


df.info()


# In[ ]:





# # processing the data

# data description for numerical value

# In[27]:


df.describe()


# #Teams availble in the data

# In[28]:


df['team1'].unique()


# Total matches availble in data

# In[29]:


df['id'].count()


# IPL seasons availble in data

# In[30]:


df['season'].unique()


# #How many time team won toss and taken feild or bat

# In[32]:


toss_dec =df.toss_decision.value_counts()
toss_dec


# In[54]:


df.toss_decision.value_counts().plot(kind='pie')


# #Teams who won toss and match

# In[33]:


toss_winner = data['toss_winner'] == data['winner']
loss , win = toss_winner.groupby(toss_winner).size()
print(win)


# #Higest number of matches won by teams in each season

# In[34]:


dg=df
grouper = dg.groupby(['season','winner'])
l=[]
for name,group in grouper:
    l.append([name[0],name[1],group['winner'].count()])
df_g=pd.DataFrame(l,columns=['year','team','wins'])
print(df_g.loc[df_g['wins'] == df_g['wins'].max()])


# In[36]:


m=df_g.groupby('year')
for n , g in m:
    print(g.loc[g['wins'] == g['wins'].max()])
    print('\n')


# #most number of matches win by the team

# In[38]:


match_win = df.winner.value_counts()
match_win


# In[39]:


sns.barplot(y = match_win.index, x = match_win)


# #most man of the match taken by player top 10

# In[40]:


most_manofmatch=df.groupby('player_of_match')
top_10_manofmatch=most_manofmatch['player_of_match'].agg(['count']).sort_values(['count'], ascending=False).head(10)
top_10_manofmatch


# #Matches played at various venus

# In[42]:


matches_played_ven =df.venue.value_counts()
matches_played_ven


# In[53]:


#sns.barplot(y = matches_played_ven.index, x = matches_played_ven)
df.venue.value_counts().plot(kind='bar')


# #Team winning by maximum wickects

# In[45]:


df.iloc[df[df['win_by_wickets'].ge(1)].win_by_wickets.idxmax()]


# #Team wining by maximum runs

# In[47]:


df.iloc[df[df['win_by_runs'].ge(1)].win_by_runs.idxmax()]


# #Matches in which duckworth lewis method applyed

# In[49]:


non_dl,dl = df.dl_applied.value_counts()
dl


# In[50]:


df.dl_applied.value_counts().plot(kind='pie')


# In[ ]:




