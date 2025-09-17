#!/usr/bin/env pybricks-micropython

from bot import Bot

if __name__ == "__main__":
    bot = Bot()
    bot.actuate_arm(actuation_value=150)
    bot.robot.straight(400)
    bot.robot.turn(-40)
    bot.robot.straight(300)
    bot.robot.straight(-50)
    bot.actuate_arm(True, actuation_value=150)
    #bot.robot.turn(-180)
    bot.robot.straight(-400)
    bot.robot.turn(-140)
    bot.robot.straight(350)
    
# fowards
# turn left
# forwards
# backwards
# turn right
# forwards
