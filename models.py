from sqlalchemy import create_engine, Column, Integer, String, Time, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import db_session, engine


Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))


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


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

