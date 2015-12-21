from app import db
from app.models import Users,A,B,C,D,Start,End,Case
import bcrypt
import argparse
from generate_fake_data import generate_data

parser = argparse.ArgumentParser(description="Initialize the database, optionally delete old data")
parser.add_argument("--delete-db",type=bool, help="if you already had a copy of the database and just want to play with different data")

args = parser.parse_args()

#initialize database
db.create_all()

#create admin account
password = bcrypt.hashpw("12345",bcrypt.gensalt())
admin_user = Users("ericschlesva@gmail.com",password,False)
db.session.add(admin_user)
db.session.commit()

#throw away old data
if args.delete_db:
    tables = [A,B,C,D,Start,End,Case]
    [table.query.delete() for table in tables]

generate_data(30)



