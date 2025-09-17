#!/usr/bin/env pybricks-micropython

from bot import Bot

if __name__ == "__main__":
    b = Bot()
    b.robot.straight(700)
    b.actuate_arm()
    b.robot.straight(-300)
    b.actuate_arm(True)
    b.robot.straight(-400)