#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Python Crash Course
# 
# Please note, this is not meant to be a comprehensive overview of Python or programming in general, if you have no programming experience, you should probably take my other course: [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/?couponCode=PY20) instead.
# 
# **This notebook is just a code reference for the videos, no written explanations here**
# 
# This notebook will just go through the basic topics in order:
# 
# * Data types
#     * Numbers
#     * Strings
#     * Printing
#     * Lists
#     * Dictionaries
#     * Booleans
#     * Tuples 
#     * Sets
# * Comparison Operators
# * if, elif, else Statements
# * for Loops
# * while Loops
# * range()
# * list comprehension
# * functions
# * lambda expressions
# * map and filter
# * methods
# ____

# ## Data types
# 
# ### Numbers

# In[1]:


1 + 1


# In[ ]:





# In[2]:


1 * 3


# In[ ]:





# In[3]:


1 / 2


# In[ ]:





# In[4]:


2 ** 4


# In[ ]:





# In[5]:


4 % 2


# In[ ]:





# In[6]:


5 % 2


# In[ ]:





# In[7]:


(2 + 3) * (5 + 5)


# In[ ]:





# ### Variable Assignment

# In[11]:


# Can not start with number or special characters
name_of_var = 2


# In[ ]:





# In[8]:


x = 2
y = 3


# In[ ]:





# In[9]:


z = x + y


# In[ ]:





# In[10]:


z


# In[ ]:





# ### Strings

# In[12]:


'single quotes'


# In[ ]:





# In[13]:


"double quotes"


# In[ ]:





# In[14]:


" wrap lot's of other quotes"


# In[ ]:





# ### Printing

# In[15]:


x = 'hello'


# In[ ]:





# In[16]:


x


# In[ ]:





# In[17]:


print(x)


# In[ ]:





# In[18]:


num = 12
name = 'Sam'


# In[ ]:





# In[19]:


print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))


# In[ ]:





# In[20]:


print('My number is: {}, and my name is: {}'.format(num,name))


# In[ ]:





# ### Lists

# In[21]:


[1,2,3]


# In[ ]:





# In[22]:


['hi',1,[1,2]]


# In[ ]:





# In[23]:


my_list = ['a','b','c']


# In[ ]:





# In[24]:


my_list.append('d')


# In[ ]:





# In[25]:


my_list


# In[ ]:





# In[26]:


my_list[0]


# In[ ]:





# In[27]:


my_list[1]


# In[ ]:





# In[28]:


my_list[1:]


# In[ ]:





# In[29]:


my_list[:1]


# In[ ]:





# In[30]:


my_list[0] = 'NEW'


# In[ ]:





# In[31]:


my_list


# In[ ]:





# In[32]:


nest = [1,2,3,[4,5,['target']]]


# In[ ]:





# In[33]:


nest[3]


# In[ ]:





# In[34]:


nest[3][2]


# In[ ]:





# In[35]:


nest[3][2][0]


# In[ ]:





# ### Dictionaries

# In[36]:


d = {'key1':'item1','key2':'item2'}


# In[ ]:





# In[37]:


d


# In[ ]:





# In[38]:


d['key1']


# In[ ]:





# ### Booleans

# In[39]:


True


# In[ ]:





# In[40]:


False


# In[ ]:





# ### Tuples 

# In[41]:


t = (1,2,3)


# In[ ]:





# In[42]:


t[0]


# In[ ]:





# In[45]:


t[0] ="NEW"


# In[ ]:





# In[ ]:





# In[ ]:





# ### Sets

# In[46]:


{1,2,3}


# In[ ]:





# In[47]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# In[ ]:





# ## Comparison Operators

# In[48]:


1 > 2


# In[ ]:





# In[49]:


1 < 2


# In[ ]:





# In[50]:


1 >= 1


# In[ ]:





# In[51]:


1 <= 4


# In[ ]:





# In[52]:


1 == 1


# In[ ]:





# In[53]:


'hi' == 'bye'


# In[ ]:





# ## Logic Operators

# In[54]:


(1 > 2) and (2 < 3)


# In[ ]:





# In[55]:


(1 > 2) or (2 < 3)


# In[ ]:





# In[56]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[ ]:





# ## if,elif, else Statements

# In[57]:


if 1 < 2:
    print('Yep!')


# In[ ]:





# In[58]:


if 1 < 2:
    print('yep!')


# In[ ]:





# In[59]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[ ]:





# In[60]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[ ]:





# In[61]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')


# In[ ]:





# ## for Loops

# In[62]:


seq = [1,2,3,4,5]


# In[ ]:





# In[63]:


for item in seq:
    print(item)


# In[ ]:





# In[64]:


for item in seq:
    print('Yep')


# In[ ]:





# In[65]:


for jelly in seq:
    print(jelly+jelly)


# In[ ]:





# ## while Loops

# In[66]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# In[ ]:





# ## range()

# In[67]:


range(5)


# In[ ]:





# In[68]:


for i in range(5):
    print(i)


# In[ ]:





# In[69]:


list(range(5))


# In[ ]:





# ## list comprehension

# In[70]:


x = [1,2,3,4]


# In[ ]:





# In[71]:


#cach1
out = []
for item in x:
    out.append(item**2)
print(out)


# In[ ]:





# In[72]:


#cach 2 [item**2 for item in x]


# In[ ]:





# ## functions

# In[73]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)


# In[ ]:





# In[74]:


my_func


# In[ ]:





# In[75]:


my_func()


# In[ ]:





# In[76]:


my_func('new param')


# In[ ]:





# In[77]:


my_func(param1='new param')


# In[ ]:





# In[78]:


def square(x):
    return x**2


# In[ ]:





# In[79]:


out = square(2)


# In[ ]:





# In[80]:


print(out)


# In[ ]:





# ## lambda expressions

# In[81]:


def times2(var):
    return var*2


# In[ ]:





# In[82]:


times2(2)


# In[ ]:





# In[83]:


lambda var: var*2


# In[ ]:





# ## map and filter

# In[84]:


seq = [1,2,3,4,5]


# In[ ]:





# In[85]:


map(times2,seq)


# In[ ]:





# In[86]:


list(map(times2,seq))


# In[ ]:





# In[87]:


list(map(lambda var: var*2,seq))


# In[ ]:





# In[88]:


filter(lambda item: item%2 == 0,seq)


# In[ ]:





# In[89]:


list(filter(lambda item: item%2 == 0,seq))


# In[ ]:





# ## methods

# In[90]:


st = 'hello my name is Sam'


# In[ ]:





# In[91]:


st.lower()


# In[ ]:





# In[92]:


st.upper()


# In[ ]:





# In[93]:


st.split()


# In[ ]:





# In[94]:


tweet = 'Go Sports! #Sports'


# In[ ]:





# In[95]:


tweet.split('#')


# In[ ]:





# In[96]:


tweet.split('#')[1]


# In[ ]:





# In[97]:


d


# In[ ]:





# In[98]:


d.keys()


# In[ ]:





# In[99]:


d.items()


# In[ ]:





# In[100]:


lst = [1,2,3]


# In[ ]:





# In[101]:


lst.pop()


# In[ ]:





# In[102]:


lst


# In[ ]:





# In[103]:


'x' in [1,2,3]


# In[ ]:





# In[104]:


'x' in ['x','y','z']


# In[ ]:





# # Great Job!
