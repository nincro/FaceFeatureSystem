# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:10:07 2019

@author: Administrator
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, TEXT

Base = declarative_base()


class Face(Base):
    
    def __init__(self,face_path=None):
    
        return
    
    __tablename__ = 'face'
    face_id = Column(Integer, primary_key=True, autoincrement=True)
    
    face_path = Column(String(length=255), nullable=True)
    
    face_uploader_id = Column(Integer)
    
    is_del = Column(Integer)
    
    face_feature = Column(TEXT)
    
    
    def __str__(self):
        return str(self.face_id)+","+str(self.face_path)+","+str(self.face_uploader_id)+","+str(self.is_del)+";"
    
    
    
class FaceService:
    # 由于脸部特征抽取的读取和写入不太频繁
    # 因此没有使用数据库的连接池，而是使用短链接
    def __init__(self,engine=None):
        if engine is None:
            engine = create_engine("mysql+pymysql://root:123456@localhost:3306/how2java?charset=utf8")
        self.DBSession = sessionmaker(bind=engine)
        return
    def getImgDir(self, face):
        session = self.DBSession()
        res_face = session.query(Face).filter(Face.face_id==face.face_id).first()
        if res_face is not None :
            face_path = res_face.face_path
        session.close()
        return face_path
    def writeFeatures(self, face):
        session = self.DBSession()
        res_face = session.query(Face).filter(Face.face_id==face.face_id).first()
        if res_face is not None :
            res_face.face_feature = face.face_feature
        session.commit()
        return res_face
    def updateFace(self, face):
        session = self.DBSession()
        result = session.query(Face).update(face)
        print(result)
        session.close()
        return result
    
from .feature_extraction import compare

def demo():
#    conn = connector.connect(user='root', password='123456', database='how2java', use_unicode=True)
#    cursor = conn.cursor()
#    mysql+pymysql://${username}:${password}@localhost:3306/${database}
    engine = create_engine("mysql+pymysql://root:123456@localhost:3306/how2java?charset=utf8")
#    engine = create_engine("mysql://root:root@localhost/how2java?charset=utf8")
#    sql_qry = "select * from face"
#    cursor.execute(sql_qry)
#    result = engine.execute(sql_qry)
#    print(result.fetchall())
    
    face_service = FaceService(engine)
    
    face = Face()
    face.face_id = 2
    face.is_del=0
    
#    face_service.insertFace(face);
    
    result = face_service.getImgDir(face);
    print(result)
    return 
if __name__ == '__main__':
    demo();