import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

import matplotlib 
matplotlib.rc('xtick', labelsize=5) 
matplotlib.rc('ytick', labelsize=10) 


raw_data = pd.read_csv('faac2016.csv')

data = raw_data[:37][['STATE', 'JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']]
states = data.iloc[:, 0]
barjan = data.iloc[:, 1]
barfeb = data.iloc[:, 2]
barmar = data.iloc[:, 3]
barapr = data.iloc[:, 4]
barmay = data.iloc[:, 5]
barjun = data.iloc[:, 6]
barjul = data.iloc[:, 7]
baraug = data.iloc[:, 8]
barsep = data.iloc[:, 9]
baroct = data.iloc[:, 10]
barnov = data.iloc[:, 11]
bardec = data.iloc[:, 12]

indx = np.arange(len(data))

plt.figure(figsize=(20, 10))

graphjan = plt.bar(x=indx, height=barjan, width=0.5)
graphfeb = plt.bar(x=indx, height=barfeb, width=0.5, bottom=barjan)
graphmar = plt.bar(x=indx, height=barmar, width=0.5, bottom=barfeb+barjan)
graphapr = plt.bar(x=indx, height=barapr, width=0.5, bottom=barmar+barfeb+barjan)
graphmay = plt.bar(x=indx, height=barmay, width=0.5, bottom=barapr+barmar+barfeb+barjan)
graphjun = plt.bar(x=indx, height=barjun, width=0.5, bottom=barmay+barapr+barmar+barfeb+barjan)
graphjul = plt.bar(x=indx, height=barjul, width=0.5, bottom=barjun+barmay+barapr+barmar+barfeb+barjan)
graphaug = plt.bar(x=indx, height=baraug, width=0.5, bottom=barjul+barjun+barmay+barapr+barmar+barfeb+barjan)
graphsep = plt.bar(x=indx, height=barsep, width=0.5, bottom=baraug+barjul+barjun+barmay+barapr+barmar+barfeb+barjan)
graphoct = plt.bar(x=indx, height=baroct, width=0.5, bottom=barsep+baraug+barjul+barjun+barmay+barapr+barmar+barfeb+barjan)
graphnov = plt.bar(x=indx, height=barnov, width=0.5, bottom=baroct+barsep+baraug+barjul+barjun+barmay+barapr+barmar+barfeb+barjan)
graphdec = plt.bar(x=indx, height=bardec, width=0.5, bottom=barnov+baroct+barsep+baraug+barjul+barjun+barmay+barapr+barmar+barfeb+barjan)


plt.xlabel('States')
plt.ylabel('FAAC Allocation (in 100 Billion)')

states = ['\n'.join(wrap(state, 15)) for state in states]



plt.xticks(indx, states)

plt.title('2016 FAAC ALLOCATION PER MONTH')



plt.show()
