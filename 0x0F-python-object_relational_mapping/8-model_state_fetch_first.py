#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password and database
Before you run the script, execute:
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # python query
    first_instance = session.query(State).order_by(State.id).first()
    if first_instance:
        print("{:d}: {:s}".format(first_instance.id, first_instance.name))
    else:
        print("Nothing")

    session.close()
