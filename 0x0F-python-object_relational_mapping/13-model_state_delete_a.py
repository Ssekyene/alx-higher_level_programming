#!/usr/bin/python3
"""
delete from table states with names containing letter 'a'
parameters given to script: username, password, database
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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # find all appropriate states to be deleted
    states = session.query(State).filter(State.name.like('%a%')).all()
    for s in states:
        session.delete(s)

    session.commit()
    session.close()
