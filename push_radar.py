#!/usr/bin/env pybricks-micropython

from bot import Bot

if __name__ == "__main__":
    bot = Bot()
    bot.robot.straight(480)
    bot.robot.turn(-30)
    bot.robot.straight(400)
    bot.robot.turn(-150)
    bot.robot.straight(600)
# fowards
# turn left
# forwards
# backwards
# turn right
# forwards
