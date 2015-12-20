from app import db
from app.models import Data
from datetime import datetime
from random import randint

def main():
    first_names = ["John","Charlie","Bob","Rick","Steven","Eric","Alex","Rachel","Sarah","Margie","Maggie","Albert"]
    last_names = ["Johnson","Harding","Phillips","Stevens","Richardson","Archer","Black","Brown","Steele","Powers"]
    for i in xrange(50):
        first_name = first_names[randint(0,len(first_names)-1)]
        last_name = last_names[randint(0,len(last_names)-1)]
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
