from app import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    marks = db.relationship('Mark', backref='students')

    def __repr__(self):
        return f"<Student {self.name}>"


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    teacher = db.Column(db.String())

    tests = db.relationship('Test', backref='courses')

    def __repr__(self):
        return f"<Course {self.name}>"


class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer())
    course_id = db.Column(db.Integer(), db.ForeignKey('courses.id'))

    marks = db.relationship('Mark', backref='tests')


class Mark(db.Model):
    __tablename__ = 'marks'

    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer())
    test_id = db.Column(db.Integer(), db.ForeignKey('tests.id'))
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id'))
