; Auto-generated. Do not edit!


(cl:in-package duckietown_msgs-msg)


;//! \htmlinclude CoordinationClearanceETHZ17.msg.html

(cl:defclass <CoordinationClearanceETHZ17> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CoordinationClearanceETHZ17 (<CoordinationClearanceETHZ17>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CoordinationClearanceETHZ17>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CoordinationClearanceETHZ17)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name duckietown_msgs-msg:<CoordinationClearanceETHZ17> is deprecated: use duckietown_msgs-msg:CoordinationClearanceETHZ17 instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <CoordinationClearanceETHZ17>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckietown_msgs-msg:header-val is deprecated.  Use duckietown_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <CoordinationClearanceETHZ17>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckietown_msgs-msg:status-val is deprecated.  Use duckietown_msgs-msg:status instead.")
  (status m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<CoordinationClearanceETHZ17>)))
    "Constants for message type '<CoordinationClearanceETHZ17>"
  '((:NA . -1)
    (:WAIT . 0)
    (:GO . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'CoordinationClearanceETHZ17)))
    "Constants for message type 'CoordinationClearanceETHZ17"
  '((:NA . -1)
    (:WAIT . 0)
    (:GO . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CoordinationClearanceETHZ17>) ostream)
  "Serializes a message object of type '<CoordinationClearanceETHZ17>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'status)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CoordinationClearanceETHZ17>) istream)
  "Deserializes a message object of type '<CoordinationClearanceETHZ17>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CoordinationClearanceETHZ17>)))
  "Returns string type for a message object of type '<CoordinationClearanceETHZ17>"
  "duckietown_msgs/CoordinationClearanceETHZ17")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CoordinationClearanceETHZ17)))
  "Returns string type for a message object of type 'CoordinationClearanceETHZ17"
  "duckietown_msgs/CoordinationClearanceETHZ17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CoordinationClearanceETHZ17>)))
  "Returns md5sum for a message object of type '<CoordinationClearanceETHZ17>"
  "863863237538fdb5f0d38c0c62b294db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CoordinationClearanceETHZ17)))
  "Returns md5sum for a message object of type 'CoordinationClearanceETHZ17"
  "863863237538fdb5f0d38c0c62b294db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CoordinationClearanceETHZ17>)))
  "Returns full string definition for message of type '<CoordinationClearanceETHZ17>"
  (cl:format cl:nil "Header header~%int8 status~%~%int8 NA=-1~%int8 WAIT=0~%int8 GO=1~%~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CoordinationClearanceETHZ17)))
  "Returns full string definition for message of type 'CoordinationClearanceETHZ17"
  (cl:format cl:nil "Header header~%int8 status~%~%int8 NA=-1~%int8 WAIT=0~%int8 GO=1~%~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CoordinationClearanceETHZ17>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CoordinationClearanceETHZ17>))
  "Converts a ROS message object to a list"
  (cl:list 'CoordinationClearanceETHZ17
    (cl:cons ':header (header msg))
    (cl:cons ':status (status msg))
))
