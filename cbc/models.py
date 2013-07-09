from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from . import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_stories_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Stories(DeclarativeBase):
    """Sqlalchemy stories model"""
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True)  # lint:ok
    title = Column('title', String)
    # desc = Column('descr', String, nullable=True)
    link = Column('link', String, nullable=True)
    comments_open = Column('comments_open', Boolean, nullable=True)
    crawled_on = Column('crawled_on', DateTime, nullable=True)


def create_comments_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Comments(DeclarativeBase):
    """Sqlalchemy comments model"""
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)  # lint:ok
    story_id = Column('story_id', Integer, nullable=True)
    comm_text = Column('comm_text', String)
    #t_up = Column('t_up', Integer, nullable=True)
    #t_down = Column('t_down', Integer, nullable=True)
    user_name = Column('user_name', String, nullable=True)
    #user_link = Column('user_link', String, nullable=True)