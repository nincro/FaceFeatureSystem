# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 22:18:23 2019

@author: Administrator
"""
from concurrent.futures import ThreadPoolExecutor
from services.Receiver import Receiver

def run():
    # 开2个线程做消费和feature
    executor = ThreadPoolExecutor()
    receiver = Receiver()
    executor.submit(receiver.run())
    
    
    return 

if __name__ == '__main__':
    run()
    