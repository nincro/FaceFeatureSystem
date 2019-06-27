# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:22:04 2019

@author: Administrator
"""
from concurrent.futures import ThreadPoolExecutor
from services.Receiver import Receiver
class Controller:
    def __init__(self):
        
        return
        
    def run(self):
        executor = ThreadPoolExecutor()
        receiver = Receiver()
        executor.submit(receiver.run())
#        executor.submit(receiver.run())
        
        return
    
    
if __name__ == '__main__':
    controller = Controller()
    controller.run()
    