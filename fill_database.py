from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from make_database import *

engine = create_engine('sqlite:///complaints.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# CLEAR OLD DB
session.query(Category).delete()
session.query(Items).delete()
session.query(User).delete()

# ADD USERS
User1 = User(name="Admin",
              email="admin@admin.com",
              picture='')
session.add(User1)
session.commit()

User2 = User(name="Manager",
              email="manager@admin.com",
              picture='')
session.add(User2)
session.commit()

# CREATE COMPLAINT CATEGORY
Category1 = Category(name="Noise",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Crime",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Garbage",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Pests",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Heating",
                      user_id=1)
session.add(Category5)
session.commit()

# The followng adds dummy data to database
Item1 = Items(name="777 Billder St - 2017-09-03 00:18:00",
               date=datetime.datetime.now(),
               description="Loud music being played",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="894 Road Ave. - 2017-09-03 00:14:02",
               date=datetime.datetime.now(),
               description="No heating in building",
               category_id=5,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="344 Road Ave. - 2017-09-03 00:14:00",
               date=datetime.datetime.now(),
               description="10 large garbage bags found on sidewalk",
               category_id=3,
               user_id=1)
session.add(Item3)
session.commit()

Item4 = Items(name="344 Road Ave. - 2017-09-03 00:12:00",
               date=datetime.datetime.now(),
               description="10 large garbage bags are talking",
               category_id=1,
               user_id=2)
session.add(Item4)
session.commit()

Item4 = Items(name="312 Street Ave. - 2017-09-03 00:12:00",
               date=datetime.datetime.now(),
               description="Lunch money seen stolen",
               category_id=2,
               user_id=2)
session.add(Item4)
session.commit()

Item4 = Items(name="01 Long Lane - 2017-09-02 00:12:00",
               date=datetime.datetime.now(),
               description="10ft Boombox with music",
               category_id=1,
               user_id=2)
session.add(Item4)
session.commit()
print "Information added to DB"