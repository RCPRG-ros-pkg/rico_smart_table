#!/usr/bin/env python3.8

import csv
import rospy 
from sensor_msgs.msg import Image

currentMeasurement = None

def saveMeasure(data): 
      
    print('Data from /topic_name received') 
    currentMeasurement = data.data
  
def getMeasure():
    if input() == " ":
        with open('dane.txt', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(currentMeasurement)

    rospy.spin()

def main(): 
      
    rospy.init_node('measures_saver', anonymous=True) 
    rospy.Subscriber("/table/raw_image", Image, saveMeasure) 
    getMeasure() 
  

if __name__ == '__main__': 
      
    try: 
        main() 
    except rospy.ROSInterruptException: 
        pass
