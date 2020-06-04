from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json
import os, fnmatch


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/images/metadata/<name>', methods=['GET'])
def getMetaData(name):
    metadataName = '../resources/metadata/%s.json' % name
    with open(metadataName) as f:
        data = json.load(f)
    return data

@app.route('/images/<name>', methods=['GET'])
def getImage(name):
    imageName = '../resources/images/%s.jpg' % name
    return send_file(imageName, mimetype='image/gif')

@app.route('/images/list', methods=['GET'])
def getImageList():
    arr = fnmatch.filter(os.listdir('../resources/images'), '*.jpg')
    arr = [os.path.splitext(file)[0] for file in arr]
    return json.dumps(arr);


if __name__ == '__main__':
    app.run()
