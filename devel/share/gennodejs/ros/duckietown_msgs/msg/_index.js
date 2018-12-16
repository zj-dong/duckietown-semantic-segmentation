
"use strict";

let Twist2DStamped = require('./Twist2DStamped.js');
let Segment = require('./Segment.js');
let StopLineReading = require('./StopLineReading.js');
let DuckieSensor = require('./DuckieSensor.js');
let SegmentList = require('./SegmentList.js');
let LEDDetectionArray = require('./LEDDetectionArray.js');
let ObstacleImageDetectionList = require('./ObstacleImageDetectionList.js');
let AprilTagDetectionArray = require('./AprilTagDetectionArray.js');
let ObstacleType = require('./ObstacleType.js');
let Pose2DStamped = require('./Pose2DStamped.js');
let LEDInterpreter = require('./LEDInterpreter.js');
let ObstacleImageDetection = require('./ObstacleImageDetection.js');
let TagInfo = require('./TagInfo.js');
let AntiInstagramTransform = require('./AntiInstagramTransform.js');
let AntiInstagramTransform_CB = require('./AntiInstagramTransform_CB.js');
let StreetNameDetection = require('./StreetNameDetection.js');
let LEDDetection = require('./LEDDetection.js');
let Trajectory = require('./Trajectory.js');
let CoordinationSignal = require('./CoordinationSignal.js');
let IntersectionPose = require('./IntersectionPose.js');
let IntersectionPoseImg = require('./IntersectionPoseImg.js');
let CoordinationSignalETHZ17 = require('./CoordinationSignalETHZ17.js');
let TurnIDandType = require('./TurnIDandType.js');
let BoolStampedETHZ17 = require('./BoolStampedETHZ17.js');
let BoolStamped = require('./BoolStamped.js');
let WheelsCmdStamped = require('./WheelsCmdStamped.js');
let CoordinationClearance = require('./CoordinationClearance.js');
let LanePose = require('./LanePose.js');
let SceneSegments = require('./SceneSegments.js');
let KinematicsParameters = require('./KinematicsParameters.js');
let LEDDetectionDebugInfo = require('./LEDDetectionDebugInfo.js');
let ObstacleProjectedDetectionList = require('./ObstacleProjectedDetectionList.js');
let FSMState = require('./FSMState.js');
let Rect = require('./Rect.js');
let Rects = require('./Rects.js');
let SignalsDetection = require('./SignalsDetection.js');
let MaintenanceState = require('./MaintenanceState.js');
let ThetaDotSample = require('./ThetaDotSample.js');
let AprilTagDetection = require('./AprilTagDetection.js');
let WheelsCmd = require('./WheelsCmd.js');
let Pixel = require('./Pixel.js');
let CoordinationClearanceETHZ17 = require('./CoordinationClearanceETHZ17.js');
let AprilTagsWithInfos = require('./AprilTagsWithInfos.js');
let CarControl = require('./CarControl.js');
let VehiclePose = require('./VehiclePose.js');
let Vector2D = require('./Vector2D.js');
let KinematicsWeights = require('./KinematicsWeights.js');
let StreetNames = require('./StreetNames.js');
let SourceTargetNodes = require('./SourceTargetNodes.js');
let ObstacleProjectedDetection = require('./ObstacleProjectedDetection.js');
let AntiInstagramHealth = require('./AntiInstagramHealth.js');
let IntersectionPoseImgDebug = require('./IntersectionPoseImgDebug.js');
let SignalsDetectionETHZ17 = require('./SignalsDetectionETHZ17.js');
let Twist2DStampedETHZ17 = require('./Twist2DStampedETHZ17.js');
let Vsample = require('./Vsample.js');
let VehicleCorners = require('./VehicleCorners.js');

module.exports = {
  Twist2DStamped: Twist2DStamped,
  Segment: Segment,
  StopLineReading: StopLineReading,
  DuckieSensor: DuckieSensor,
  SegmentList: SegmentList,
  LEDDetectionArray: LEDDetectionArray,
  ObstacleImageDetectionList: ObstacleImageDetectionList,
  AprilTagDetectionArray: AprilTagDetectionArray,
  ObstacleType: ObstacleType,
  Pose2DStamped: Pose2DStamped,
  LEDInterpreter: LEDInterpreter,
  ObstacleImageDetection: ObstacleImageDetection,
  TagInfo: TagInfo,
  AntiInstagramTransform: AntiInstagramTransform,
  AntiInstagramTransform_CB: AntiInstagramTransform_CB,
  StreetNameDetection: StreetNameDetection,
  LEDDetection: LEDDetection,
  Trajectory: Trajectory,
  CoordinationSignal: CoordinationSignal,
  IntersectionPose: IntersectionPose,
  IntersectionPoseImg: IntersectionPoseImg,
  CoordinationSignalETHZ17: CoordinationSignalETHZ17,
  TurnIDandType: TurnIDandType,
  BoolStampedETHZ17: BoolStampedETHZ17,
  BoolStamped: BoolStamped,
  WheelsCmdStamped: WheelsCmdStamped,
  CoordinationClearance: CoordinationClearance,
  LanePose: LanePose,
  SceneSegments: SceneSegments,
  KinematicsParameters: KinematicsParameters,
  LEDDetectionDebugInfo: LEDDetectionDebugInfo,
  ObstacleProjectedDetectionList: ObstacleProjectedDetectionList,
  FSMState: FSMState,
  Rect: Rect,
  Rects: Rects,
  SignalsDetection: SignalsDetection,
  MaintenanceState: MaintenanceState,
  ThetaDotSample: ThetaDotSample,
  AprilTagDetection: AprilTagDetection,
  WheelsCmd: WheelsCmd,
  Pixel: Pixel,
  CoordinationClearanceETHZ17: CoordinationClearanceETHZ17,
  AprilTagsWithInfos: AprilTagsWithInfos,
  CarControl: CarControl,
  VehiclePose: VehiclePose,
  Vector2D: Vector2D,
  KinematicsWeights: KinematicsWeights,
  StreetNames: StreetNames,
  SourceTargetNodes: SourceTargetNodes,
  ObstacleProjectedDetection: ObstacleProjectedDetection,
  AntiInstagramHealth: AntiInstagramHealth,
  IntersectionPoseImgDebug: IntersectionPoseImgDebug,
  SignalsDetectionETHZ17: SignalsDetectionETHZ17,
  Twist2DStampedETHZ17: Twist2DStampedETHZ17,
  Vsample: Vsample,
  VehicleCorners: VehicleCorners,
};
