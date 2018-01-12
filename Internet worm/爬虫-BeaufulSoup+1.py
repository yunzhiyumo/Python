
# coding: utf-8

# In[82]:

from urllib.request import urlopen
from bs4 import BeautifulSoup

h = urlopen('http://www.woshipm.com/pd/900844.html').read().decode('utf-8')
print(h)

soup = BeautifulSoup(h,features='lxml')
a_targ = soup.find_all('a')
for l in a_targ:
    print(l['href'])

