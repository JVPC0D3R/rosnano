#include <ros.h>
#include <std_msgs/Float32.h>
#include <Servo.h>

ros::NodeHandle nh;

Servo xServo;
Servo yServo;

int X_SERVO_PIN = 3;
int Y_SERVO_PIN = 5;

void xAngleCallback(const std_msgs::Float32& msg) {
  // Set the x-axis servo position based on the received angle
  int xAngle = msg.data;
  xServo.write(xAngle);
}

void yAngleCallback(const std_msgs::Float32& msg) {
  // Set the y-axis servo position based on the received angle
  int yAngle = msg.data;
  yServo.write(yAngle);
}

ros::Subscriber<std_msgs::Float32> xAngleSub("x_axe_angle", xAngleCallback);
ros::Subscriber<std_msgs::Float32> yAngleSub("y_axe_angle", yAngleCallback);

void setup() {
  // Initialize the ROS node
  nh.initNode();
  
  // Attach the servos to the corresponding pins
  xServo.attach(X_SERVO_PIN);
  yServo.attach(Y_SERVO_PIN);

  // Subscribe to the angle topics
  nh.subscribe(xAngleSub);
  nh.subscribe(yAngleSub);
}

void loop() {
  // Process any incoming ROS messages
  nh.spinOnce();

  // Other code for the main loop, if needed
}
