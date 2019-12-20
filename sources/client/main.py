from tkinter import Canvas, Tk, Button, messagebox
from tkinter import *
import random
from PIL import Image, ImageTk
from dataclasses import dataclass
from objects.UFO import Ufo
from objects.cloud import Cloud
from const_client import *
import json

class Client:
    """Base client class.
    """
    def __init__(self, trace_path):
        """Initialising values and creating the window with game world
        """
        self.trace_path = trace_path
        self.game_data = json.loads(open(trace_path, 'r').read())

        self.root = Tk()
        self.root.title("RAINBOW hit")
        self.canvas = Canvas(self.root, width=WIDTH * 1.8, height=HEIGHT, bg="white")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i == 0 or j == 0 or i == GRID_SIZE - 1 or j == GRID_SIZE - 1:
                    continue
                self.canvas.create_rectangle(i * CELL_SIZE, j * CELL_SIZE,
                                             i * CELL_SIZE + CELL_SIZE,
                                             j * CELL_SIZE + CELL_SIZE, fill='pink', outline='#999090')
        self.canvas.create_rectangle(32, 32, HEIGHT - 32, HEIGHT - 32, outline='black', width=2)
        self.canvas.grid(column=0, row=0)
        pilImage1 = Image.open("./sources/client/assets/ufo1.png")
        self.image1 = ImageTk.PhotoImage(pilImage1)
        self.canvas.create_image(592, 48, image=self.image1)
        self.health1 = self.canvas.create_rectangle(630, 36, 1010, 58, fill='green')
        pilImage2 = Image.open("./sources/client/assets/ufo2.png")
        self.image2 = ImageTk.PhotoImage(pilImage2)
        self.canvas.create_image(592, 90, image=self.image2)
        self.health2 = self.canvas.create_rectangle(630, 78, 1010, 100, fill='green')
        # self.text = self.canvas.create_text(632, 138, font="Times", text='Enter Your code:')
        # message_entry = Text(width=56, height=22)
        # message_entry.place(x=566, y=168)
        # self.window = self.canvas.create_rectangle(566, 168, 1018, 524, width=5, outline='#f21d1d')
        # message_button = Button(text="Send", width=64)
        # message_button.place(x=564, y=540)

    def get_object(self, x, y):
        for obj in self.objects:
            if self.canvas.coords(obj) == (48 + x * 32, 32 * 18 - (48 + y * 32)):
                return obj
        return None

    def get_ufo_by_name(self, name):
        for obj in self.objects:
            if isinstance(obj, Ufo):
                if obj.name == name:
                    return obj
        return None
    
    def creating_game_objects(self):
        """Creating Ufos and clouds
        """
        self.objects = []
        for k, v in self.game_data[0]['init_world'].items():
            x, y = eval(k) 
            if v[0] == 'Bot' and v[1] == 'player1':
                self.objects.append(Ufo(48 + x * 32, 32 * 18 - (48 + y * 32), self.canvas, "./sources/client/assets/ufo1.png", 'player1'))
            elif v[0] == 'Bot' and v[1] == 'player2':
                self.objects.append(Ufo(48 + x * 32, 32 * 18 - (48 + y * 32), self.canvas, "./sources/client/assets/ufo2.png", 'player2'))
            else:
                self.objects.append(Cloud(48 + x * 32, 32 * 18 - (48 + y * 32), self.canvas, "./sources/client/assets/Cloud.png"))            
        
        self.game_data.pop(0)

    def actions(self):
        """Commands processing and visualising actions: move, fire
        """
        self.root.bind('1' + '<Right>', self.ufo_1.move)
        self.root.bind('2' + '<Right>', self.ufo_2.move)
        self.root.bind('<Down>', self.ufo_2.laser)
        self.root.bind('<Up>', self.ufo_2.deleter)

    def updater(self):
        if list(self.game_data[0].keys())[0] == 'sleep':
            self.canvas.after(1000, self.updater)
        elif list(self.game_data[0].keys())[0] == 'step':
            player = self.game_data[0]['step']['player']
            newx = self.game_data[0]['step']['new_x']
            newy = self.game_data[0]['step']['new_y']

            player_ufo = self.get_ufo_by_name(player)
            player_ufo.move(newx, newy)

            self.canvas.after(1000, self.updater)
        elif list(self.game_data[0].keys())[0] == 'shoot':
            player = self.game_data[0]['shoot']['player']
            x_end = self.game_data[0]['shoot']['x_end']
            y_end = self.game_data[0]['shoot']['y_end']
            destroyed = self.game_data[0]['shoot']['destroyed']

            player_ufo = self.get_ufo_by_name(player)
            player_ufo.laser(x_end, y_end)

            self.canvas.after(1000, self.updater)
        elif list(self.game_data[0].keys())[0] == 'game_over':
            pass

    def main_loop(self):
        self.canvas.after(1000, self.updater)
        self.root.mainloop()
