import pickle
f = open('data.dat','rb')
t = pickle.load(f)
L = t[0]
maxim = t[1]
f.close()
n = len(L)
lat = 'lat'
lng = 'lng'
for i in range(n):
	for j in range(i,n-1):
		if (L[j][lat] > L[j+1][lat]):
			L[j] , L[j+1] = L[j+1], L[j]
		elif (L[j][lat] == L[j+1][lat]):
			if (L[j][lng] > L[j+1][lng]):
				L[j] , L[j+1] = L[j+1] , L[j]
	print (i)
f = open('data2.dat','wb')
pickle.dump((L,maxim),f)


print L[:20]