from flask import Flask, make_response, request, abort, jsonify, render_template
from flask_cors import CORS
#from api import make_soft_prediction, transform_input
#import numpy as np

app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/sentiment_score', methods=['GET','POST'])
def get_sentiment_score():
    score = 90
    inputs = ''
    if request.method == 'GET':
        args = request.args
        # Initialize default values
        long,lat,time = 0,0,0
        long,lat,time = args['long'],args['lat'],args['time']
        print(long,lat,time)
    else:
        if not request.json:
            abort(400)

        inputs = request.get_json()
        long,lat,time = inputs['long'],inputs['lat'],inputs['time']
        print(long,lat,time)

    #inputs = list(map(float, inputs))
    # score = make_soft_prediction(inputs)
    # score = round(float(score),2)
    response = {
        'review': inputs,
        'score': score
    }

    print("response is: {}".format(response))

    return jsonify(response), 201

# @app.route('/')
# def index():
#     return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)