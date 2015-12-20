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
    va_id = db.Column(db.Integer)
    name = db.Column(db.String(400))
    email = db.Column(db.String(500))
    
    def __init__(self,name,email,va_id):
        self.name = name
        self.email = email
        self.va_id = va_id
    
#Internal Data
#The ingress point for the caseflow system
class Start(db.Model):
    __tablename__ = 'start'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_created = db.Column(db.DateTime)

    def __init__(self,date_created):
        self.date_created = date_created
    
    def __repr__(self):
        return "<Start %r>" % str(self.va_id)

class End(db.Model):
    __tablename__ = 'end'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_concluded = db.Column(db.DateTime)
    
    def __init__(self,date_concluded):
        self.date_concluded = date_concluded
    
    def __repr__(self):
        return "<End %r>" % str(self.va_id)

class A(db.Model):
    __tablename__ = 'a'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed):
        self.date_started = date_started
        self.date_completed = date_completed
    def __repr__(self):
        return "<A %r>" % str(self.va_id)

class B(db.Model):
    __tablename__ = 'b'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed):
        self.date_started = date_started
        self.date_completed = date_completed

    def __repr__(self):
        return "<B %r>" % str(self.va_id)

class C(db.Model):
    __tablename__ = 'c'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed):
        self.date_started = date_started
        self.date_completed = date_completed

    def __repr__(self):
        return "<C %r>" % str(self.va_id)

class D(db.Model):
    __tablename__ = 'd'
    id = db.Column(db.Integer,primary_key=True)
    va_id = db.ForeignKey("case.va_id")
    date_started = db.Column(db.DateTime)
    date_completed = db.Column(db.DateTime)
    
    def __init__(self,date_started,date_completed):
        self.date_started = date_started
        self.date_completed = date_completed

    def __repr__(self):
        return "<D %r>" % str(self.va_id)

