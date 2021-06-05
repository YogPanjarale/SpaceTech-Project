import pandas as pd
from flask import Flask,request
from flask.json import jsonify
from  dataclasses import dataclass

stars = []
@dataclass
class Star():
    name:str
    distance:float
    mass:float
    radius:str
    gravity:str
    def to_dict(self):
        return {
            'name':self.name,
            'distance':self.distance,
            'mass':self.mass,
            'radius':self.radius,
            'gravity':self.gravity,
        }

df = pd.read_csv('filtered_stars.csv') 

for i in range(len(df)):
    n = df['Star_name'][i]
    d = df['Distance'][i]
    m = df['Mass'][i]
    r = df['Radius'][i]
    g = df['Gravity'][i]
    stars.append(Star(n,d,m,r,g).to_dict())

app = Flask(__name__)

@app.get('/all')
def getAll():
    return jsonify(stars)

@app.get('/star')
def getStarByName():
    starname = request.args.get('name','NotFound')
    # print(stars)
    star = list(filter(lambda p: p['name'].lower() == starname.lower(), stars))
    return jsonify(star if star else "Star Not Found")
if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)


