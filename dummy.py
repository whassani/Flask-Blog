import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///dbMyBlog.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password")
session.add(user)

category = Category("category-1")
session.add(category)

category = Category("category-2")
session.add(category)

post = Post("title-1", "description-1", "body-1", "1")
session.add(post)

post = Post("title-2", "description-2", "body-2", "2")
session.add(post)


# commit the record the database
session.commit()

session.commit()
