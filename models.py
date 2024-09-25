from sqlalchemy import Column, Integer, Float, Date, DateTime, Boolean, String, Table, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, session, sessionmaker
from datetime import datetime

Base = declarative_base()

Session = sessionmaker()
session = Session()

"""
likes_news = Table(
    "likes_news",
    Column("news_id", Integer, ForeignKey('news.id'), primary_key=True, nullable=False),
    Column("users_id", Integer, ForeignKey('users.id'), primary_key=True, nullable=False)    
)
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    profile = relationship("Profile", uselist=False, backref="user") # [<Profile 1>]
    #news = relationship("New", backref="user")
    friends = relationship("User", secondary="friends_users")

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    biography = Column(Text)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)

class New(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="news")
    categories = relationship("Category", secondary="categories_news")

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)
    date_message = Column(DateTime, default=datetime.now())
    news_id = Column(Integer, ForeignKey('news.id'))
    users_id = Column(Integer, ForeignKey('users.id'))

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    news = relationship("New", secondary="categories_news")


# Modelo

class CategoryNew(Base):
    __tablename__ = 'categories_news'
    news_id = Column(Integer, ForeignKey('news.id'), primary_key=True, nullable=False)
    categories_id = Column(Integer, ForeignKey('categories.id'), primary_key=True, nullable=False)

class FriendUser(Base):
    __tablename__ = 'friends_users'
    users_id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)
    friends_id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)

class LikeNew(Base):
    __tablename__ = 'likes_news'
    news_id = Column(Integer, ForeignKey('news.id'), primary_key=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)