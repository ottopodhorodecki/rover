#!/usr/bin/env pybricks-micropython

from bot import Bot

if __name__ == "__main__":
    bot = Bot()
    bot.actuate_arm()
    bot.robot.straight(400)
    bot.robot.turn(-40)
    bot.robot.straight(400)
    bot.robot.turn(-180)
    bot.robot.straight(400)
    bot.robot.turn(30)
    bot.robot.straight(400)
# fowards
# turn left
# forwards
# backwards
# turn right
# forwards
