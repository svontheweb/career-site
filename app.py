from flask import Flask, render_template, jsonify

JOBS = [
  {
    'id': 0,
    'title': 'Software Engineer',
    'location': 'Bengluru, IN',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 1,
    'title': 'Frontend Engineer',
    'location': 'Pune, IN',
    'salary': 'Rs. 7,00,000'
  },
  {
    'id': 2,
    'title': 'Backend Engineer',
    'location': 'California, US',
    'salary': '$ 50,000'
  },
  {
    'id': 3,
    'title': 'Cloud Architect',
    'location': 'Hyderabad, IN'
  },
  {
    'id': 4,
    'title': 'AWS Engineer',
    'location': 'Nevada, US',
    'salary': '$ 80,000'
  }
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS, company_name = 'Topmate')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
# entry point
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
