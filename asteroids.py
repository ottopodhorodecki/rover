#!/usr/bin/env pybricks-micropython

from bot import Bot


def fetch_item_straight_line(b: Bot):
    distance = b.move_whilst_not_near(min_distance=100, interval=50)
    b.robot.straight(60)
    b.actuate_arm()
    b.robot.straight(-distance)
    b.robot.turn(180)
    b.actuate_arm(reversing=True)
    b.robot.turn(180)


def fetch_all_asteroids(b: Bot):
    b.robot.turn(-35)
    fetch_item_straight_line(b)
    b.robot.turn(130)
    fetch_item_straight_line(b)
    b.robot.turn(50)
    fetch_item_straight_line(b)


if __name__ == '__main__':
    bot = Bot()
    fetch_all_asteroids(bot)
