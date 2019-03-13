#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #Importing the data for analysis from matches.csv

# In[5]:


data= pd.read_csv('matches.csv')


# #verifying the columns availble in the data

# In[6]:


data.columns


# #checking the top two rows availble in the data

# In[7]:


data.head(2)


# In[ ]:





# # pre processing the data required for analysis

# Removing the non required feilds from the data

# In[8]:


data=data.drop(['umpire1','umpire2','umpire3'],axis=1)


# In[9]:


data.head(2)


# #Removing the null value if any

# In[10]:


data.shape


# In[11]:


data =data.dropna(how='all')


# In[12]:


data.shape  #there are no rows where all element are null


# checking  the types of data avaible 

# In[13]:


data.info()


# #converting date type from object to datetime

# In[14]:


data['date']= pd.to_datetime(data['date']) 


# In[15]:


data.info()


# #create the backup of the data

# In[16]:


df = data


# In[17]:


df.info()


# In[ ]:





# # processing the data

# data description for numerical value

# In[18]:


df.describe()


# #Teams availble in the data

# In[19]:


df['team1'].unique()


# Total matches availble in data

# In[20]:


df['id'].count()


# IPL seasons availble in data

# In[21]:


df['season'].unique()


# #How many time team won toss and taken feild

# In[30]:


field,bat =df.toss_decision.value_counts()
field


# In[23]:


df.toss_decision.value_counts().plot(kind='pie')


# #Teams who won toss and match

# In[24]:


toss_winner = data['toss_winner'] == data['winner']
loss , win = toss_winner.groupby(toss_winner).size()
print(win)


# #Higest number of matches won by teams in each season

# In[28]:


dg=df
grouper = dg.groupby(['season','winner'])
l=[]
for name,group in grouper:
    l.append([name[0],name[1],group['winner'].count()])
df_g=pd.DataFrame(l,columns=['year','team','wins'])
#print(df_g.loc[df_g['wins'] == df_g['wins'].max()])


# In[53]:


m=df_g.groupby('year')
t=[]
for n , g in m:
    print(g.loc[g['wins'] == g['wins'].max()])
    print('\n')


# #most number of matches win by the team

# In[94]:


match_win = df.winner.value_counts().max()
print(df.iloc[match_win][10],'   ', match_win)


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

# In[77]:


max_wicket = df.iloc[df[df['win_by_wickets'].ge(1)].win_by_wickets.idxmax()]
max_wicket


# #Team wining by maximum runs

# In[83]:


max_run =df.iloc[df[df['win_by_runs'].ge(1)].win_by_runs.idxmax()]
max_run


# #Matches in which duckworth lewis method applyed

# In[75]:


non_dl,dl = df.dl_applied.value_counts()
dl


# In[50]:


df.dl_applied.value_counts().plot(kind='pie')


# unit testing for obtained result

# In[62]:


assert all (df.columns==['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2',
       'umpire3'])


# #number of team opteded for feliding after winning the toss
# 

# In[65]:


#df.toss_decision.value_counts()
assert (field == 413)


# #Team winning by maximum wickects

# In[82]:


import numpy as np
test=max_wicket.iloc[10]
np.testing.assert_array_equal(test,"Kolkata Knight Riders")


# #team who won the toss and also won match

# In[66]:


assert (win == 357)


# #Team wining by maximum runs

# In[86]:


test1= max_run.iloc[10]
np.testing.assert_array_equal(test1,'Mumbai Indians')


# #most number of matches win by the team

# In[97]:


test2= df.iloc[match_win][10]
np.testing.assert_array_equal(test2,'Mumbai Indians')


# #Matches in which duckworth lewis method applyed

# In[89]:


assert(dl == df.dl_applied.value_counts()[1])


# In[ ]:




