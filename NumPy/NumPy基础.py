
# coding: utf-8

# ### 测试numpy安装成功

# In[35]:


from numpy import *


# In[36]:


a = random.rand(4,4)


# In[37]:


print(a)


# ### Numpy函数库中存在2种数据类型，矩阵matrix 和 数组array

# ### mat（）函数可将数组转为矩阵

# In[38]:


b = mat(a)


# In[39]:


print(b)


# ### .I操作符实现矩阵的求逆运算

# In[41]:


c = b.I


# In[42]:


print(c)


# In[43]:


a*c


# ### markdown 单元格还支持 LaTex 语法。例如：$$\int_0^{+\infty} x^2 dx$$
