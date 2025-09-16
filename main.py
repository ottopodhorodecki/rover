#!/usr/bin/env pybricks-micropython

from bot import Bot
from time import sleep


def reset_arm(b: Bot):
    b.actuate_arm()


def convert_wheel_angle(target_angle: int) -> int:
    return target_angle * 4


def fetch_item_straight_line(b: Bot):
    distance = b.move_whilst_not_near(min_distance=40, interval=50)
    b.actuate_arm()
    b.robot.straight(-distance)
    print("rotating 1")
    b.robot.turn(180)
    b.actuate_arm(reversing=True)
    print("rotating 2")
    b.robot.turn(180)


def main():
    b = Bot()
    fetch_item_straight_line(b)
    #b.rotate(convert_wheel_angle(90))
    #reset_arm(b)
    #input()
    #b.ev3.speaker.beep()
    #fetch_item_straight_line(b)
    # b.move_whilst_not_near(min_distance=100, interval=10)
    #print(b.gyro.speed(), b.gyro.angle())
    #b.robot.straight(10)
    #b.robot.turn(360)
    #print(b.ultrasonic.distance(silent=False))
    #b.ev3.speaker.beep() 


if __name__ == "__main__":
    main()
