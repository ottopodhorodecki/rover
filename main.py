#!/usr/bin/env pybricks-micropython

from bot import Bot
from time import sleep


def find_item(b: Bot):
    print()


def push_block(b: Bot):
    print()


def reset_arm(b: Bot):
    b.actuate_arm()


def fetch_item_straight_line(b: Bot):
    b.actuate_arm(reversing=True)
    distance = b.move_whilst_not_near(min_distance=90, interval=20)
    b.actuate_arm()
    b.robot.straight(-distance)


def main():
    b = Bot()
    fetch_item_straight_line(b)
    # b.move_whilst_not_near(min_distance=100, interval=10)
    #print(b.gyro.speed(), b.gyro.angle())
    #b.robot.straight(10)
    #b.robot.turn(360)
    #print(b.ultrasonic.distance(silent=False))
    #b.ev3.speaker.beep()


if __name__ == "__main__":
    main()