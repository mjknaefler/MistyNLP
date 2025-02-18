# First import the robot object
from mistyPy import Robot

if __name__ == "__main__":
    ip_address = "192.168.1.125"
    # Create an instance of a robot
    misty = Robot(ip_address)