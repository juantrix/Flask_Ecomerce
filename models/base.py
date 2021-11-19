from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///db/data_base.sqlite')


Session = sessionmaker(bind = engine)


Base = declarative_base()