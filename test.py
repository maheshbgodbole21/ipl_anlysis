from IPl_Analysis_1 import *
# In[62]:


assert all (df.columns==['id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue'])


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
np.testing.assert_array_equal(test2,'Mumbai Indian')


# #Matches in which duckworth lewis method applyed

# In[89]:


assert(dl == df.dl_applied.value_counts()[1])
