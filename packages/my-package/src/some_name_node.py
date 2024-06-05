#!/usr/bin/env python

# import external libraries
import rospy

# import libraries which are part of the package (i.e. in the include dir)
import library

# import DTROS-related classes
from duckietown.dtros import \
    DTROS, \
    NodeType, \
    TopicType, \
    DTReminder,\
    DTParam, \
    ParamType

# import messages and services
from std_msgs.msg import Float32
from duckietown_msgs.msg import \
    SegmentList, \
    Segment, \
    BoolStamped

class SomeNameNode(DTROS):
    def __init__(self, node_name):
        super(SomeNameNode, self).__init__(
            node_name=node_name,
            node_type=NodeType.PERCEPTION
        )
        
        # Setting up parameters
        self.detection_freq = DTParam(
            '~detection_freq',
            param_type=ParamType.INT,
            min_value=-1,
            max_value=30
        )
        # ...
        
        # Generic attributes
        self.something_happened = None
        self.arbitrary_counter = 0
        # ...

        # Subscribers
        self.sub_img = rospy.Subscriber(
            'image_rect', 
            Image, 
            self.cb_img
        )
        self.sub_cinfo = rospy.Subscriber(
            'camera_info', 
            CameraInfo, 
            self.cb_cinfo
        )
        # ...

        # Publishers
        self.pub_img = rospy.Publisher(
            'tag_detections_image/compressed',
            CompressedImage,
            queue_size=1,
            dt_topic_type=TopicType.VISUALIZATION
        )
        self.pub_tag = rospy.Publisher(
            'tag_detections', 
            AprilTagDetectionArray, 
            queue_size=1,
            dt_topic_type=TopicType.PERCEPTION
        )
        # ...

if __name__ == '__main__':
    some_name_node = SomeNameNode(node_name='same_name_node')
    rospy.spin()