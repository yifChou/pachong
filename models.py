from sqlalchemy import create_engine,MetaData,Column,Integer,String,Table,ForeignKey,UniqueConstraint,Index,TIMESTAMP,Boolean,Date,Time,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from  datetime import datetime
import time
engine  = create_engine("mysql+pymysql://root:8597121@127.0.0.1:3306/music", max_overflow=5)
Base = declarative_base()
class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer,primary_key=True)
    musicid = Column(String(200))
    title = Column(String(200))
    image = Column(String(400))
    singer = Column(String(120))
    album = Column(String(150))
    pubdate = Column(String(20))
    comments = Column(Integer)
    creattime = Column(DateTime)
    updatetime = Column(DateTime)
def init_db():
    Base.metadata.create_all(engine)
def drop_db():
    Base.metadata.drop_all(engine)
#drop_db()
#init_db()
Session = sessionmaker(bind=engine)
session = Session()
