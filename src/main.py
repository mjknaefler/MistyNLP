import sys
import os

# Add the mistyPy submodule to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../third_party/Python-SDK")))

# First import the robot object
from mistyPy import Robot


if __name__ == "__main__":
    ip_address = "192.168.1.125"
    # Create an instance of a robot
    misty = Robot(ip_address)
    print("Connection to Misty established.")