import math
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor, Stop
from pybricks.parameters import Direction
from pybricks.robotics import DriveBase

from config import ULTRASONIC_PORT, WHEEL_DIAMETER, AXLE_TRACK, GYRO_PORT, ARM_PORT, L_WHEEL_PORT, R_WHEEL_PORT, ROTATION_COMPENSATION


class Bot:
    def __init__(self):
        self._ev3 = EV3Brick()
        self._left_motor = Motor(L_WHEEL_PORT)
        self._right_motor = Motor(R_WHEEL_PORT)
        self._arm_motor = Motor(ARM_PORT)
        self._robot = DriveBase(self._left_motor, self._right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
        self._ultrasonic = UltrasonicSensor(ULTRASONIC_PORT)
        self._gyro = GyroSensor(GYRO_PORT, Direction.CLOCKWISE)
        self._coords = [0, 0]
        self._rotation = 0

    def is_near(self, min_distance: int) -> bool:
        return self.ultrasonic.distance(silent=False) < min_distance

    def move_whilst_not_near(self, min_distance: int, interval: int) -> int:
        distance_moved = 0
        while not self.is_near(min_distance):
            self.robot.straight(interval)
            distance_moved += interval

        return distance_moved

    def actuate_arm(self, reversing: bool = False):
        d = -170 if not reversing else 170
        self._arm_motor.run_angle(100, d, then=Stop.HOLD, wait=True)
        self._arm_motor.hold()

    def update_coords(self, distance):
        rad = math.radians(self._rotation)
        self._coords[0] += distance * math.cos(rad)
        self._coords[1] += distance * math.sin(rad)
    
    def update_rotation(self, angle):
        self._rotation += angle
    
    def go_home(self):
        self.rotate(-self._rotation)
        self.move_forward(math.sqrt(self._coords[1]**2 + self._coords[0]**2))
    
    def rotate(self, degrees: float):
        self._left_motor.run_angle(100, degrees, wait=True)
        self._right_motor.run_angle(100, ROTATION_COMPENSATION, wait=True)
        self._rotation += degrees

    @property
    def robot(self) -> DriveBase:
        return self._robot
    
    @property
    def ev3(self) -> EV3Brick:
        return self._ev3
        
    @property
    def ultrasonic(self) -> UltrasonicSensor:
        return self._ultrasonic

    @property
    def gyro(self) -> GyroSensor:
        return self._gyro

    @property
    def is_level(self) -> bool:
        return self.gyro.angle() >= 10
