# Bigger value = maze with more spaces
LABYRINTH_DENSITY: int = 3

# Kill user-code thread, if it is in inactive state for more than n seconds
THREAD_TIMEOUT: int = 2

# max amount of steps per game
MAX_STEPS: int = 80

# side of a cell
CELL_SIDE: int = 32

FIELD_X: int = 16

FIELD_Y: int = 16

# fov of a bot measured in cells
BOT_FOV_CELLS: int = 5

# default bot hp
BOT_DEFAULT_HP: int = 10

# delta
DELTA: float = .5

# Max possible coordinate
MAX_COORD: int = 1_000_000

# default laser damage
LASER_DAMAGE: int = 1

# is debug
IS_DEBUG: bool = False

# ansi terminal colors: cyan
ANSI_CYAN: str = '\u001b[36m'

# ansi terminal colors: green
ANSI_GREEN: str = '\u001b[32m'

# ansi terminal colors: reset
ANSI_RES: str = '\u001b[0m'

TRACE_NAME: str = 'history.json'

INIT_WORLD_CMD = '''{{
    "init_world" : 
    {{
{}
    }}
}}'''

SLEEP_CMD = '''{{
    "sleep": {{
        "player": "{}"
    }}
}}'''

STEP_CMD = '''{{
    "step" : {{
        "player": "{}",
        "new_x": {},
        "new_y": {}
    }}
}}
'''

SHOOT_CMD = '''{{
    "shoot" : {{
        "player": "{}",
        "x_start": {},
        "y_start": {},
        "x_end": {},
        "y_end": {},
        "destroyed": {}
    }}
}}
'''

GAME_OVER = '''{{
    "game_over":
    {{
        "winner": "{}",
        "draw": {}
    }}
}}
'''

BOTS_STATE = '''{{
    "bot_state":
    {{
        "name": "{}",
        "hp": {}
    }}
}}
'''
