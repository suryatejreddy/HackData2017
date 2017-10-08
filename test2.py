import pickle
import pandas as pd
import ast
f = open('data.dat','rb')
t = pickle.load(f)
L = t[0]
maxim = t[1]
f.close()


df = pd.DataFrame(L)


result = df.sort_values(['lat', 'lng'], ascending=[1, 0])



L = result.values.tolist()

newL = []
c = 0
for i in L:
	d = dict()
	d['count'] = i[0]
	d['lat'] = i[1]
	d['lng'] = i[2]
	c = (c+1)%4
	if c==3:
		continue
	newL.append(d)


f = open('dataFinal.dat','wb')
pickle.dump((newL,maxim),f)

f.close()

# result =  pd.sort(['lat', 'lng'], ascending=[1, 0])
