from engine.gameobjects.bots.bot import Bot
from typing import Any, List
import exceptions

def continuemain(func):
    '''
    Decorator, that should be added automatically for any user-code
    First argument should be bot instance
    '''
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        if isinstance(args[0], Bot):
            args[0].main_event.set()
        else:
            raise exceptions.InvalidSelfInstance('Invalid type of self object!')
        return ret
    return wrapper

@continuemain
def run_user(bot: Bot):
    # user code starts here
    bot.step(1)
    bot.step(3)
    bot.step(5)
    bot.step(7)
    bot.sleep()
    bot.sleep()
    bot.sleep()
    bot.sleep()
    bot.step(8)

@continuemain
def run_enemy(bot: Bot):
    bot.step(2)
    bot.step(4)
    bot.step(6)
    bot.step(6)
    bot.step(8)
    bot.step(10)
    bot.step(12)

@continuemain
def run_enemy2(bot: Bot):
    def step_more(n: int):
        for i in range(n):
            bot.step(1)
    step_more(5)
    # TODO: if thread hangs kill it
    while True:
       pass
    step_more(5)
    
