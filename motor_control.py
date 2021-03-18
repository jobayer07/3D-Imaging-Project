from zaber_motion import Library
from zaber_motion.binary import Connection
Library.enable_device_db_store()
from zaber_motion import Units
from zaber_motion import RotationDirection


with Connection.open_serial_port("COM3") as connection:
    device_list = connection.detect_devices()
    print("Found {} Rotating Stage".format(len(device_list)))
    device = device_list[0]
    #For homing the device
    device.home()
    # Move to the 10 degree
    device.move_absolute(10, Units.ANGLE_DEGREES, RotationDirection.CLOCKWISE) #RotationDirection.COUNTERCLOCKWISE
    print('done1')
    # Move by an additional 20 degree
    device.move_relative(20, Units.ANGLE_DEGREES)
    print('done2')

