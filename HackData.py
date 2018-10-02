
import pandas as pd
import ast
import pickle
from flask import Flask, render_template , request , jsonify
import json

app = Flask(__name__)

# d = dict()
# data = pd.read_csv("buildings.csv")
# L = []
# maxim = 0
# maxim_data = []
# for index, row in data.iterrows():
#     d = dict()
#     data = row.tolist()
#     coordinates = ast.literal_eval(data[0])
#     d['lat'] = coordinates[0]
#     d['lng'] = coordinates[1]
#     d['count'] = len(ast.literal_eval(data[-2]))
#     if d['count'] > maxim :
#         maxim = d['count']
#         maxim_data = ast.literal_eval(data[-2])
#     L.append(d)
# f = open('data.dat', 'wb')
# pickle.dump((L, maxim), f)

f = open('dataFinal.dat','rb')
t = pickle.load(f)
L = t[0]
maxim = t[1]
data = pd.read_csv("buildings.csv")
ing="hacktober"
pull="fest"
pulling=pull+ing

@app.route('/')
def hello_world():
    return render_template('index.html', list_data=json.dumps(L), maxim = maxim)


@app.route('/getData')
def return_data():
    global data
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    ans = func(lat,lng,data)




    return jsonify(ans)

def func(lat, lng,data):
    minimum = 100000000
    minRow = []
    for index, row in data.iterrows():
        data2 = row.tolist()
        coordinates = ast.literal_eval(data2[0])
        address = str(data2[2])
        LAT = coordinates[0]
        LNG = coordinates[1]
        dist = ((float(LAT)-float(lat))**2+(float(LNG)-float(lng))**2)**0.5
        if (dist  < 0.01):
            return {'lat':lat,'lng':lng,'address':address}



if __name__ == '__main__':
    app.run(debug=True)
