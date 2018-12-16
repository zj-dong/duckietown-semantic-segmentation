#! /usr/bin/env python
import argparse
import tensorflow as tf
import numpy as np
#import cv2
import visualize
import time
import matplotlib.pyplot as plt
import rospy
#from semantic_segmentation.msg import segmentation_results
from sensor_msgs.msg import Image
from std_msgs.msg import Empty
import os
from tqdm import trange
from utils.config import Config
from model import ICNet, ICNet_BN
from cv_bridge import CvBridge, CvBridgeError
import sys
from PIL import Image as Im

model_config = {'train': ICNet, 'trainval': ICNet, 'train_bn': ICNet_BN, 'trainval_bn': ICNet_BN, 'others': ICNet_BN}

# Choose dataset here, but remember to use `script/downlaod_weight.py` first
dataset = 'cityscapes'
filter_scale = 1
    
class InferenceConfig(Config):
    def __init__(self, dataset, is_training, filter_scale):
    	Config.__init__(self, dataset, is_training, filter_scale)
    
    # You can choose different model here, see "model_config" dictionary. If you choose "others", 
    # it means that you use self-trained model, you need to change "filter_scale" to 2.
    model_type = 'trainval'

    # Set pre-trained weights here (You can download weight from Google Drive) 
    model_weight = 'icnet_cityscapes_trainval_90k.npy'
    
    # Define default input size here
    INFER_SIZE = (1024, 2048, 3)




class SemanticSegmentationNode:
    def __init__(self):
        model_config = {'train': ICNet, 'trainval': ICNet, 'train_bn': ICNet_BN, 'trainval_bn': ICNet_BN, 'others': ICNet_BN}
        dataset = 'cityscapes'
        filter_scale = 1
        cfg = InferenceConfig(dataset, is_training=False, filter_scale=filter_scale)
        self.label1 = 4
        self.label2 = 5
		# Create graph here 
        model = model_config[cfg.model_type]
        net = model(cfg=cfg, mode='inference')
		# Create session & restore weight!
        net.create_session()
        net.restore(cfg.model_weight)
        self.net=net
        self.cfg=cfg
        
        self.__bridge = CvBridge()
        # Publisher to publish predicted image
        self.__image_pub = rospy.Publisher('/'+os.environ['DUCKIEBOT_NAME']+'/prediction_images', Image, queue_size=1)
        # Publisher to publish the result of classes
        #self.__result_pub = rospy.Publisher('/'+os.environ['DUCKIEBOT_NAME'] +"/predicted_result", segmentation_results, queue_size=1)
        # Subscribe to topic which will kick off object detection in the next image
        self.__command_sub = rospy.Subscriber('/'+os.environ['DUCKIEBOT_NAME'] + "/start", Empty, self.StartCallback)
        # Subscribe to the topic which will supply the image fom the camera
        self.__image_sub = rospy.Subscriber('/'+ os.environ['DUCKIEBOT_NAME'] + "/camera_node/image/raw", Image, self.Imagecallback)

        # Flag to indicate that we have been requested to use the next image
        self.__scan_next = True		
  

        # Read the confidence level, any object with a level below this will not be used
        # This parameter is set in the config.yaml file
        #confidence_level = rospy.get_param('/object_detection/confidence_level', 0.50)
        # Create the object_detection_lib class instance
        #self.__odc = object_detection_lib.ObjectDetection(confidence_level)
        #self.__semseg = 

    # Callback for start command message
    def StartCallback(self, data):
        # Indicate to use the next image for the scan
        self.__scan_next = True
    
    
    def get_labels(self, im2): 
        im1=im2          
        #cfg.display()
        
        #print (im1.shape)
        # Create graph here 
        cfg = self.cfg
        
        
        # Create session & restore weight!
        
        #im1 = cv2.imread('./data/input/cityscapes1.png')
        im=Im.fromarray(im1)
        #print(im1.shape)
        #print(im.size)
        if im1.shape != cfg.INFER_SIZE:
            #print('**********************')
            #im1 = cv2.resize(im1, (cfg.INFER_SIZE[1], cfg.INFER_SIZE[0]))
            im=im.resize([cfg.INFER_SIZE[1], cfg.INFER_SIZE[0]])
            im1=np.array(im)
        #print (im1.shape)
        results1 = self.net.predict(im1)
        overlap_results1 = 0.5 * im1 + 0.5 * results1[0]
        vis_im1 = np.concatenate([im1, results1[0], overlap_results1], axis=1)
        
        #print(vis_im1.shape)
        results = np.uint8(vis_im1)

        
    #    results_shape = np.array([results1.shape[1],results1.shape[2]])
    #    results2 = visualize.decode_labels(results1,results_shape,19)
    #    results2 = tf.Session().run(results2)
    #    overlap_results1 = 0.5 * im1 + 0.5 * results2[0]
    #    vis_im1 = overlap_results1
    #    plt.figure(figsize=(20, 15))
    #    plt.imshow(vis_im1)
        
        
        
        return results



    # Callback for new image received
    def Imagecallback(self, data):
        # if self.__scan_next == True:
        print("WORKS!")
        rospy.loginfo("Predicting")
        self.__scan_next = False
        # Convert the ROS image to an OpenCV image
        image = self.__bridge.imgmsg_to_cv2(data, "bgr8")

        # The supplied image will be modified if known objects are detected
        # Predict result, the result will be drawn to `image`
        #self.__odc.scan_for_objects(image)

        
        # publish the image, it may have been modified
        # try:
        image_message = self.__bridge.cv2_to_imgmsg(self.get_labels(image),encoding="bgr8")
        
        rospy.loginfo("Finish prediction")
        self.__image_pub.publish(image_message)

            # except CvBridgeError as e:
            #     print(e)

            # Publish names of objects detected
            # result = detection_results()
            # result.names_detected = object_names_detected
            # self.__result_pub.publish(result)

def main(args):
    rospy.init_node('tf_semantic_segmentation_node', anonymous=False)
    # initialize class ObjectDetectionNode
    _ = SemanticSegmentationNode()
    rospy.loginfo("tf semantic segmentation node started")
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)







