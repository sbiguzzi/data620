#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as net
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


G = net.Graph()


# In[3]:


labels = {
    0:'Stefano',
    1:'Beverly',
    2:'Carol',
    3:'Diane',
    4:'Ed',
    5:'Fernando',
    6:'Garth',
    7:'Heather',
    8:'Ike',
    9:'Jane',
}


# In[4]:


edges = [(0,1),(0,2),(0,3),(0,5),(1,3),(1,4),(1,6),(2,3),(2,5),(3,4),(3,5),(3,6),(4,6),(5,6),(5,7),         (6,7),(7,8),(8,9)]


# In[5]:


G.add_edges_from(edges)


# In[6]:


G1 = net.relabel_nodes(G,labels)


# In[77]:


pos=net.spring_layout(G1)
net.draw(G1,with_labels=1,pos=pos)
plt.show()

