#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the db hbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password and database
Before you run the script, execute:
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # database engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # python query
    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
