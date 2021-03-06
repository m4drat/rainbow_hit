from typing import *


class GameException(Exception):
    '''Base class for all in-game exceptions.
    '''
    pass


class NetworkException(Exception):
    '''Base class for all network exceptions.
    '''
    pass


class InvalidSelfInstance(GameException):
    '''Raised, when invalid object passed in args[0]
    '''

    def __init__(self):
        GameException.__init__(self, 'Invalid type of self object!')


class StepsAreOver(GameException):
    '''Exception, which get raised, if steps are over
    '''

    def __init__(self):
        GameException.__init__(self, 'Steps are over!')


class ActionsAreOver(GameException):
    '''Exception, which get raised, if bot actions are over
    '''

    def __init__(self):
        GameException.__init__(self, 'Bot actions are over!')


class BotTimeoutError(GameException, TimeoutError):
    '''Exception, which get raised, 
    if the bot thread runs longer than it should
    '''

    def __init__(self):
        GameException.__init__(self, 'Bot thread time is over!')


class ThreadKilledError(GameException):
    '''Exception, which get raised, 
    if the user-thread was killed, and player still trying to use it
    '''

    def __init__(self):
        GameException.__init__(self, 'User thread killed!')


class FatalException(Exception):
    '''FatalError

    after this exception execution cannot be continued
    '''

    def __init__(self, msg):
        Exception.__init__(self, msg)


class GameOver(GameException):
    '''Exception, which get raised, if game is over
    '''
    game_won: bool = False
    winner: Optional[object] = None

    def __init__(self, win_status: bool, winner=None):
        self.game_won = win_status
        self.winner = winner
        GameException.__init__(self, 'Game Over')


class InvalidCoordinate(GameException):
    '''Exception, which get raised if someone try to place object at already occupied cell 
    '''

    def __init__(self):
        GameException.__init__(self, 'Invalid coordinate')


class BotIsDead(GameException):
    '''Exception, which get raised if bot is dead
    '''

    def __init__(self):
        GameException.__init__(self, 'Bot is dead!')


class HandshakeError(NetworkException):
    '''Exception, which get raised if troubles with handshake
    '''

    def __init__(self):
        NetworkException.__init__(self, 'Client did not say zdarova')


class UnameError(NetworkException):
    '''Exception, which get raised if client did not say his username
    '''

    def __init__(self):
        NetworkException.__init__(self, 'Client did not say his username')


class CodeTransmissionError(NetworkException):
    '''Exception, which get raised if troubles with code transmission
    '''

    def __init__(self):
        NetworkException.__init__(self, 'Troubles with code transmission')
