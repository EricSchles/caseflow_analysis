from app import db
from app import flask_login

#Tool login stuff
class User(flask_login.UserMixin):
    pass

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean,default=False)

    def __init__(self,email,password,authenticated=False):
        self.email = email
        self.password = password
        self.authenticated = authenticated
    def __repr__(self):
        return "<Users %r>" % str(self.email)

class Case(db.Model):
    __tablename__ = "case"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400))
    email = db.Column(db.String(500))
    start = db.relationship("Start",backref="case", lazy="dynamic")
    end = db.relationship("End",backref="case",lazy="dynamic")
    a_s = db.relationship("A",backref="case",lazy="dynamic")
    b_s = db.relationship("B",backref="case",lazy="dynamic")
    c_s = db.relationship("C",backref="case",lazy="dynamic")
    d_s = db.relationship("D",backref="case",lazy="dynamic")
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
#Internal Data
#The ingress point for the caseflow system
class Start(db.Model):
    __tablename__ = 'start'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer,db.ForeignKey("case.id"))
    date_created = db.Column(db.DateTime)

    def __init__(self,date_created,case_id):
        self.date_created = date_created
        self.case_id = case_id
        
    def __repr__(self):
        return "<Start %r>" % str(self.case_id)

class End(db.Model):
    __tablename__ = 'end'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer,db.ForeignKey("case.id"))
    date_concluded = db.Column(db.DateTime)
    
    def __init__(self,date_concluded,case_id):
        self.date_concluded = date_concluded
        self.case_id = case_id
    def __repr__(self):
        return "<End %r>" % str(self.case_id)

class A(db.Model):
    __tablename__ = 'a'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey("case.id"))
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed,case_id):
        self.date_started = date_started
        self.date_completed = date_completed
        self.case_id = case_id 
    def __repr__(self):
        return "<A %r>" % str(self.case_id)

class B(db.Model):
    __tablename__ = 'b'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer,db.ForeignKey("case.id"))
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed,case_id):
        self.date_started = date_started
        self.date_completed = date_completed
        self.case_id = case_id

    def __repr__(self):
        return "<B %r>" % str(self.case_id)

class C(db.Model):
    __tablename__ = 'c'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey("case.id"))
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed,case_id):
        self.date_started = date_started
        self.date_completed = date_completed
        self.case_id = case_id

    def __repr__(self):
        return "<C %r>" % str(self.case_id)

class D(db.Model):
    __tablename__ = 'd'
    id = db.Column(db.Integer,primary_key=True)
    case_id = db.Column(db.Integer,db.ForeignKey("case.id"))
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed,case_id):
        self.date_started = date_started
        self.date_completed = date_completed
        self.case_id = case_id

    def __repr__(self):
        return "<D %r>" % str(self.case_id)

