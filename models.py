from sqlalchemy import create_engine, Column, Integer, String, Time, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import db_session, engine
from datetime import datetime
from sqlalchemy.orm import relationship


Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    lesson = relationship("Lesson", backref="subject")


class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    time = Column(Time())
    day_of_week = Column(String(50))
    sub_id = Column(Integer, ForeignKey('subjects.id'))
    cl_id = Column(Integer, ForeignKey('classes.id'))


class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    lesson = relationship("Lesson", backref="class")


class User(Base):
    __tablename__ = "users"
    id = Column('user_id',Integer , primary_key=True)
    username = Column('username', String(20), unique=True , index=True)
    password = Column('password' , String(10))
    registered_on = Column('registered_on' , DateTime)
 
    def __init__(self , username ,password):
        self.username = username
        self.password = password
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

