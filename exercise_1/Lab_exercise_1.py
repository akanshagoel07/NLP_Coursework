from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request

import nltk

from nltk.corpus import stopwords

response = urllib.request.urlopen('https://www.spacex.com/vehicles/starship/')
#reading response
html = response.read()

print(html)

soup = BeautifulSoup(html,"html5lib")

text = soup.get_text(strip=True)
#tokenisation
tokens = [t for t in text.split()]

clean_tokens = tokens[:]

sr = stopwords.words('english')

for token in tokens:
    #removing stopwords
    if token in stopwords.words('english'):

        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

del_list = []

for key,val in freq.items():

    print (str(key) + ':' + str(val))
    #checking vo token with frequency less than 5
    if val<5:
        del_list.append(key)
#deleteing token with frequency less than 5, from dictionary
for iter in del_list:
    del freq[iter]

freq.plot(10, cumulative = False)

data_con = pd.DataFrame(freq.items(), columns=['word', 'frequency'])
print(data_con)

bch = data_con.plot.bar(x='word', y='frequency', rot=0)
plt.show()
