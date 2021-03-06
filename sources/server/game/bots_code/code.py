from ..engine.gameobjects.bots.user_bot import Bot
from ..exceptions import *


def continuemain(func):
    '''
    Decorator, that should be added automatically for any user-code
    First argument should be bot instance
    '''

    def wrapper(self, *args, **kwargs):
        try:
            self.main_event.set()

            # block current thread
            self.event.wait()
            self.event.clear()
            ret = func(self, *args, **kwargs)
            return ret
        except (StepsAreOver, ActionsAreOver, BotTimeoutError, BotIsDead) as e:
            # handle async-raised exceptions
            return e
        finally:
            # allow main thread to continue
            if isinstance(self, Bot):
                self.main_event.set()
            else:
                raise InvalidSelfInstance('Object type mismatch! Should be Bot().')

    return wrapper


def get_callable_script(name):
    return importlib.import_module(f'..bot_scripts.{name}', __name__).perform
