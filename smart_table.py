#!/usr/bin/env python3.8

import time
import os
import rospy

# Suppress tensorflow noncritical warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from nodes.table import TableNode
from sensor.sensor import Sensor
from connection.connection import Serial

if __name__ == "__main__":

    sensor = Sensor(Serial.default_port_name())
    sensor.connect_to_controller()
    node = TableNode(weight_calculation_mode="neuron", default_turn_on=True)
    node.set_sensor(sensor)
    rospy.spin()

