# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:19:05 2019

@author: Administrator
"""
from .feature_extraction import compare
import os
class FeatureExtractionService:
    def __init__(self):
        
        return
    def extract(self,model,image_path,
                    image_size=160,
                    margin=44,
                    gpu_memory_fraction=0.5
                    ):
        #    组合参数，进行调用
        args = []
        args.append(model)
        args.append(image_path)
        args = compare.parse_arguments(args)
        return compare.main(args)

    def taskFeatureExtract(self, file_path,model=None):
        print("taskFeatureExtract")
        # 根据图像路径进行处理
        if model is None and os.path.exists(model):
            model = "./models/20170512-110547.pb"
    #    image_files = ["./feature_extraction/1.png"]
        return self.extract(model,file_path)    
