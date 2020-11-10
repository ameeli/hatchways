"""
Arguments will be
passed in the following order:
{path-to-courses-file} {path-to-students-file} {path-to-tests-file} {path-to-marks-file}
{path-to-output-file}
For example:
“python main.py courses.csv students.csv tests.csv marks.csv output.json”
“java Main courses.csv students.csv tests.csv marks.csv output.json”
“node app.js courses.csv students.csv tests.csv marks.csv output.json”

- read csv files and add to some sort of data structure, db?
- read students (id, name)
- read courses (id, name, teacher)
- read tests (id, course, weight)
- read marks (test_id, student_id, mark)

- get student course from marks. if student took test with course, add course

TODO:
1. setup db connection with flask
2. setup models
3. populate db with example data
4. parse data for report card
    - unit tests
5. return report card json format
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return {"yo": "world"}


if __name__ == "__main__":
    app.run(debug=True)
