#!/usr/bin/env pybricks-micropython

from bot import Bot


def release_hammer(b: Bot):
    b.robot.straight(300)
    b.release_hammer()
    b.robot.straight(-300)


if __name__ == '__main__':
    b = Bot()
    release_hammer(b)
