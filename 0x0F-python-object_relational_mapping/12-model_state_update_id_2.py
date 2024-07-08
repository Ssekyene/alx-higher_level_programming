#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa
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
    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # python script
    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = "New Mexico"

    session.commit()
    session.close()
