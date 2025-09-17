#!/usr/bin/env pybricks-micropython

from bot import Bot


def test_turn():
    bot = Bot()
    bot.robot.turn(360)
    bot.robot.turn(-360)
