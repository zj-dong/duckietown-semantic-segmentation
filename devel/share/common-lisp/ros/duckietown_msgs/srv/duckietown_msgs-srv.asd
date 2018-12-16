
(cl:in-package :asdf)

(defsystem "duckietown_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GetVariable" :depends-on ("_package_GetVariable"))
    (:file "_package_GetVariable" :depends-on ("_package"))
    (:file "SetFSMState" :depends-on ("_package_SetFSMState"))
    (:file "_package_SetFSMState" :depends-on ("_package"))
    (:file "SetValue" :depends-on ("_package_SetValue"))
    (:file "_package_SetValue" :depends-on ("_package"))
    (:file "SetVariable" :depends-on ("_package_SetVariable"))
    (:file "_package_SetVariable" :depends-on ("_package"))
  ))