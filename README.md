# location-safety-predictor-backend

pip install virtualenv
python -m virtualenv env
source env/Scripts/activate

pip install flask

http://127.0.0.1:8000/sentiment_score?long=10&lat=20&time=30

get - https://location-safety.onrender.com/sentiment_score?long=10&lat=20&time=30

post - https://location-safety.onrender.com/sentiment_score

post payload body -

{
    "long":"10",
    "lat":"10",
    "time":"10"
}