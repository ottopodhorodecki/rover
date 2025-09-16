from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor, Stop
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

from config import ULTRASONIC_PORT, WHEEL_DIAMETER, AXLE_TRACK, GYRO_PORT, ARM_PORT, L_WHEEL_PORT, R_WHEEL_PORT


class Bot:
    def __init__(self):
        self._ev3 = EV3Brick()
        self._left_motor = Motor(L_WHEEL_PORT)
        self._right_motor = Motor(R_WHEEL_PORT)
        self._arm_motor = Motor(ARM_PORT)
        self._robot = DriveBase(self._left_motor, self._right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)
        self._ultrasonic = UltrasonicSensor(ULTRASONIC_PORT)
        self._gyro = GyroSensor(GYRO_PORT, Direction.CLOCKWISE)

    def is_near(self, min_distance: int) -> bool:
        return self.ultrasonic.distance(silent=False) < min_distance

    def move_whilst_not_near(self, min_distance: int, interval: int) -> int:
        distance_moved = 0
        while not self.is_near(min_distance):
            self.robot.straight(interval)
            distance_moved += interval

        return distance_moved

    def say_ow():
        return

    def actuate_arm(self, reversing: bool = False):
        d = 90 if not reversing else -90
        self._arm_motor.run_angle(100, d, then=Stop.HOLD, wait=True)
        self._arm_motor.hold()

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
