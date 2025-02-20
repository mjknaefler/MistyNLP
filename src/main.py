import sys
import os

# Get absolute path to MistyPy submodule
misty_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Python-SDK/mistyPy"))
if misty_path not in sys.path:
    sys.path.insert(0, misty_path)

# First import the RobotGenerator
from mistyPy.GenerateRobot import RobotGenerator

# Creating a new robot generator will rewrite the RobotCommands.py and Websocket.py 
# files to adjust them to the commands and websockets the robot has available
RobotGenerator("192.168.1.125")

# Then import the robot object
from mistyPy.Robot import Robot

if __name__ == "__main__":
    ip_address = "192.168.1.125"
    # Create an instance of a robot
    misty = Robot(ip_address)
    print("Connection to Misty established.")