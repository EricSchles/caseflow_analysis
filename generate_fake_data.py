from app import db
from app.models import Start,End,A,B,C,D
from datetime import datetime
from random import randint

def generate_firstname():
    first_names = ["John","Charlie","Bob","Rick","Steven","Eric","Alex","Rachel","Sarah","Margie","Maggie","Albert","Christine","Christina"]
    return first_names[randint(0,len(first_names)-1)]

def generate_lastname():
    last_names = ["Johnson","Harding","Phillips","Stevens","Richardson","Archer","Black","Brown","Steele","Powers"]
    return last_names[randint(0,len(last_names)-1)]

def generate_data(num_entities):    
    tables = [A,B,C,D]
    for i in xrange(num_entities):
        first_name = 
        last_name = 
        name = first_name + " " + last_name
        email = first_name+last_name+"@gmail.com"
        data = Data(
            datetime(randint(2011,2015),randint(1,10),randint(1,28),1,1),
            name,
            email
        )
        db.session.add(data)
        db.session.commit()

if __name__ == '__main__':
    main()
