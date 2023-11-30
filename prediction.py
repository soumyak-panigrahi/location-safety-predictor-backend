import pickle
import numpy as np

crimes = ['ASSAULT', 'BATTERY', 'CRIMINAL DAMAGE', 'DECEPTIVE PRACTICE', 'THEFT']
weights = [0.90625, 0.9, 0.91667, 1, 0.9375]

# 91%
p_successful_arrest = pickle.load(open('./models/probability_of_successful_arrest.pkl', 'rb'))

# 85% //5 70% //10
severity_of_crime = pickle.load(open('./models/severity_of_crime.pkl', 'rb'))

# Prob of occuring on women

p_of_being_on_women = pickle.load(open('./models/probability_of_being_on_women.pkl', 'rb'))

scaler  = pickle.load(open('./models/scaler.pkl', 'rb'))


def transform_input(input):
	return scaler.transform(np.asarray([input]))

def probability_of_successful_arrest(input):
    return p_successful_arrest.predict_proba(transform_input(input))[0,1]

def crime_type(input):
    return severity_of_crime.predict(transform_input(input))[0]

def severity(input):
    return weights[crime_type(input)]

def safety_score(input):
    return probability_of_successful_arrest(input) * severity(input)

def most_possible_crime(input):
    return crimes[crime_type(input)]

def probability_of_being_on_women(input):
    return p_successful_arrest.predict_proba(transform_input(input))[0,1]