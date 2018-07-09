from darkflow.darkflow.defaults import argHandler 
import os
from darkflow.darkflow.net.build import TFNet
import sys

FLAGS = argHandler()
FLAGS.setDefaults()

video_path = sys.argv[1]
FLAGS.demo = video_path

FLAGS.model = "darkflow/cfg/yolo.cfg"
FLAGS.load = "darkflow/bin/yolo.weights" 


FLAGS.threshold = 0.5
FLAGS.gpu = 0 
FLAGS.track = True 
FLAGS.trackObj = ['Car', 'Pedestrian', 'Dog', 'Bicycle', 'Motobike'] 

FLAGS.saveVideo = False  
FLAGS.BK_MOG = True 
FLAGS.tracker = "sort"    #we are only using sort algorithm the original code uses both deep sort and sort algorithms
FLAGS.skip = 5 
 
FLAGS.display = True 

tfnet = TFNet(FLAGS)

tfnet.camera()
exit('Demo stopped, exit.')
