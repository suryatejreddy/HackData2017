lat =  42.40089685923913 
lon =  -83.15689086914062
import pickle

d = dict()
data = pd.read_csv("buildings.csv")
L = []
maxim = 0
maxim_data = []
for index, row in data.iterrows():
    d = dict()
    data = row.tolist()
    coordinates = ast.literal_eval(data[0])
    d['lat'] = coordinates[0]
    d['lng'] = coordinates[1]
    d['count'] = len(ast.literal_eval(data[-2]))
    if d['count'] > maxim :
        maxim = d['count']
        maxim_data = ast.literal_eval(data[-2])
    L.append(d)
f = open('data.dat', 'wb')
pickle.dump((L, maxim), f)



