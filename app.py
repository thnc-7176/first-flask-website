"""
Tutorial from https://www.youtube.com/watch?v=yBDHkveJUf4&t=3558s

From: 06/11/2023 to: 
Thiago Naves Cassimiro
"""

# Imports
from flask import Flask, render_template, jsonify

# Starting Flask framework
app = Flask(__name__)

# Logics
# For the careers project
jobs_list = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'São Paulo, Brazil',
    'salary': 'R$ 6.000,00'
  },
  {
    'id': 2,
    'title': 'Front-End Engineer',
    'location': 'Remote',
    'salary': '$ 4.000,00'
  },
  {
    'id': 3,
    'title': 'Back-End Engineer',
    'location': 'New York, USA',
    'salary': '$ 4.000,00'
  },
]



# Routes
@app.route("/")
def homepage():
  return render_template('home.html')

@app.route("/carrers-homepage")
def carrers_homepage():
  return render_template('carrers-homepage.html', jobs=jobs_list)

# API route to return json data
@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs_list)

# Run
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

### I stopped at 