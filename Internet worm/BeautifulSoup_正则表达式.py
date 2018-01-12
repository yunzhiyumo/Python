
# coding: utf-8

# In[17]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re    #正则表达式

h = urlopen('http://www.hao123.com').read().decode('utf-8')
soup = BeautifulSoup(h,features='lxml')

a_targ = soup.find_all('img',{'src':re.compile('.*?\.jpg')})
for i in a_targ:
    print(i['src'])

