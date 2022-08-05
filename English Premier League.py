#!/usr/bin/env python
# coding: utf-8

# # Premier League Standings 22 Seasons (2000-2022)

# ## Context
# ##### The Premier League, often referred to as the English Premier League or the EPL (legal name: The Football Association Premier League Limited), is the top level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League (EFL). Seasons run from August to May with each team playing 38 matches (playing all 19 other teams both home and away).[1] Most games are played on Saturday and Sunday afternoons. This data included the premier league standings of the last decade

# ## Analysis
# #### Which teams have the best attacking or defensive record in the last decade ?
# #### How many points does it usually take to qualify for Europe ?
# #### Who are the underdogs of the last decade ?

# ## Pivot some rows for extra analysis in the dashboard

# In[2]:


import pandas as pd
#import file
epl=pd.read_csv("epl.csv")
#extract needed rows to be pivoted
epl2 = epl.iloc[:,[0,2,4,5,6,7,8,9,10]]
#Transform the rows using Melt
epl3 = pd.melt(epl2, id_vars=["Season","Team"])
#export the transformed rows
epl3.to_csv("English.csv",sep=",")


# ## Which teams have the best attacking or defensive record in the last decade ?

# ### Best Attack

# In[65]:


import pandas as pd
epl = pd.read_csv("epl.csv")
epl = epl.iloc[:,:11]
Best = epl[epl["Season"].between("2011-2012", "2021-2022")]


# In[91]:


BA_info = Best.sort_values(by="GF", ascending = False).head(50)
BA_info


# In[92]:


BA_info["Team"].value_counts()


# ### Best Defence

# In[93]:


BD_info = Best.sort_values(by="GA", ascending= True).head(50)
BD_info


# In[63]:


BD_info["Team"].value_counts()


# ### Team with Most Wins

# In[40]:


Most_wins = epl.loc[(epl['Pos'] == 1)]
Most_wins.head(10)


# In[43]:


Most_wins["Team"].value_counts()


# ### How many points does it usually take to qualify for Europe ?

# In[82]:


Europe = epl.iloc[:,2:].groupby("Team").mean().astype(int).sort_values(by = "Pts", ascending=False)
Europe.head(6)


# ##### Approximately 62 points is needed to qualify for Europe from EPL

# ## Teams with Most Points since 2000-2001 Season

# In[87]:


epl.iloc[:,2:].groupby("Team").sum().sort_values(by = "Pts", ascending = False)


# In[66]:


epl.head()


# In[80]:





# In[ ]:




