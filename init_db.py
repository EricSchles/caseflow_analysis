from app import db
from app.models import Users
import bcrypt
from generate_fake_data import main
#initialize database
db.create_all()

#create admin account
password = bcrypt.hashpw("12345",bcrypt.gensalt())
admin_user = Users("ericschlesva@gmail.com",password,False)
db.session.add(admin_user)
db.session.commit()
main()



