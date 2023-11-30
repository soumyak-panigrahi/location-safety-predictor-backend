from flask import Flask, make_response, request, abort, jsonify, render_template
from flask_cors import CORS
from prediction import safety_score, most_possible_crime, probability_of_being_on_women
#import numpy as np

app = Flask(__name__)
CORS(app)
app.debug = True


@app.route('/sentiment_score', methods=['GET','POST'])
def get_sentiment_score():
    score = 90
    inputs = ''
    crime = ''
    if request.method == 'GET':
        args = request.args
        # Initialize default values
        long,lat,hour,minute = 0,0,0,0
        long,lat,hour, minute = args['long'],args['lat'],args['hour'],args['minute']
        print(long,lat,hour, minute)
    else:
        if not request.json:
            abort(400)

        inputs = request.get_json()
        long,lat,hour,minute = inputs['long'],inputs['lat'],inputs['hour'],inputs['minute']
        print(long,lat,hour, minute)

    inputs = [ hour, lat, long, minute]
    
    inputs = list(map(float, inputs))
    score = safety_score(inputs)
    score = round(float(score),2)
    crime = most_possible_crime(inputs)
    women = probability_of_being_on_women(inputs)
    women = round(float(women),2)
    response = {
        'review': inputs,
        'score': score,
        'crime': crime,
        'women': women
    }

    print("response is: {}".format(response))

    return jsonify(response), 201
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)