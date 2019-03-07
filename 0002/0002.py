import re

import pymysql
from sqlalchemy import Column, String, DATE, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import base64

Base = declarative_base()

db_info = {
    'user':'test',
    'passwd':'chaianzhi',
    'ip':'localhost',
    'port':'3306',
    'database':'mytest',
}

class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(String(200), primary_key=True)
    deadline = Column(DATE)
    userID = Column(String(200))
    code = Column(String(200))

def getDbConnect(db_info):
    connect_str = 'mysql+pymysql://{user}:{passwd}@{ip}:{port}/{database}'.format_map(db_info)
    print(connect_str)
    engine = create_engine(connect_str)
    # 根据已有的所有类来创建对应的表
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(engine)
    session = DBSession()
    return session


def parse_base64(line):
    return base64.urlsafe_b64decode(line.encode('UTF-8'))


def addToDB():
    print('addToDB')
    session = getDbConnect(db_info)
    with open('coupon.txt', 'r') as file:
        for line in file.readlines():
            c_id = re.findall(r'.*/.*:(.*)\'', str(parse_base64(line)))
            print(c_id)
            session.add(Coupon(id=c_id.pop(), code=line))
        session.commit()
        session.close()



if __name__ == '__main__':
    print('0002')
    addToDB()