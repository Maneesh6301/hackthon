#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


### importing the csv  and json into sql for easy manipulation


import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv(r'C:\Users\manee\Downloads\orders.csv')

# Create Connection (replace with your password/port)
engine = create_engine('mysql+pymysql://root:123@localhost/it')

# Write to MySQL (this creates the table automatically)
df.to_sql('orders', con=engine, if_exists='replace', index=False)


# In[4]:


import pandas as pd
from sqlalchemy import create_engine

# Load JSON (it automatically flattens simple structures)
df = pd.read_json(r"C:\Users\manee\Downloads\users.json")

# Connect and Upload
engine = create_engine('mysql+pymysql://root:123@localhost/it')
df.to_sql('orders_from_json', con=engine, if_exists='replace', index=False)


# In[ ]:





# In[ ]:




