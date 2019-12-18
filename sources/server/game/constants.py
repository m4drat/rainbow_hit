# Kill user-code thread, if it is in inactive state for more than n seconds
THREAD_TIMEOUT: int = 2

# max amount of steps per game
MAX_STEPS: int = 3

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
IS_DEBUG: bool = True

# ansi terminal colors: cyan
ANSI_CYAN: str = '\u001b[36m'

# ansi terminal colors: green
ANSI_GREEN: str = '\u001b[32m'

# ansi terminal colors: reset
ANSI_RES: str = '\u001b[0m'

INIT_WORLD_CMD = '''{{
    "world" : 
    {{
{}
    }}
}}'''

SLEEP_CMD = '''{{
    "{}": {{
        "command": {{
            "sleep" : {{}},
        }}
    }}
}}'''

STEP_CMD = '''{{
    "{}": {{
        "command": {{
            "step" : {{
                "new_x": {},
                "new_y": {},
            }}
        }}
    }}
}}
'''

SHOOT_CMD = '''{{
    "{}": {{
        "command": {{
            "shoot" : {{
                "x_start": {},
                "y_start": {},
                "x_end": {},
                "y_end": {}
            }},
            "destroyed": {}
        }}
    }}
}}
'''

GAME_OVER = '''{{
    "winner": {},
    "draw": {}
}}
'''