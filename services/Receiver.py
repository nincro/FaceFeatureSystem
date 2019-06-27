# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:07:56 2019

@author: Administrator
"""

import pika
import time
from .Face import Face
from .Face import FaceService
from .FeatureExtractionService import FeatureExtractionService
import os
feature_service = FeatureExtractionService()

def callback(ch, method, propertites, body):
    #    print(" [x] Received {}".format(body))
        print("propertites:{}".format(propertites))
        print("method:{}".format(method))
        print(" [x] Received %r" % body)
    #    time.sleep(body.count(b'.'))
    #    print(" [x] Done")
    #    face_id = int(body)
        face = Face()
        face.face_id = int(body)
        face_service = FaceService()
        face_dir = face_service.getImgDir(face)
        print(face_dir)
        if face_dir is not None and os.path.exists(face_dir):
            face_feature = feature_service.taskFeatureExtract(face_dir)
            print("pass")
            face.face_feature = str(face_feature)
            face_service.writeFeatures(face)
           
        
        ch.basic_ack(delivery_tag = method.delivery_tag)
class Receiver:
    
    def __init__(self):
        return        
    
    def run(self):
        print("receiver.run")
        if self.rece is not None:
            self.rece()
        
    
        
    
    def rece(self,username='face', passwd='face'):
        u_p = pika.PlainCredentials(username, passwd)
            
        connection = pika.BlockingConnection(pika.ConnectionParameters('10.24.81.115',
                                                                      virtual_host='/face',
                                                                       credentials=u_p))
        
        channel = connection.channel()
        
        channel.queue_declare(queue='face_id')
        channel.exchange_declare(exchange='face')
        channel.queue_bind(exchange='face', queue='face_id', routing_key='face_id')
        #   注意这里的顺序
        channel.basic_qos(prefetch_count=1) #只预定一条
        channel.basic_consume('face_id', callback, auto_ack=False)
        channel.start_consuming()
