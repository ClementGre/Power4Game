import tkinter as tk

from PIL import Image, ImageTk, ImageFilter


def create_repeated_image(image, width, height):
    bg_width, bg_height = image.size
    repeated_image = Image.new('RGB', (width, height))
    for y in range(0, height, bg_height):
        for x in range(0, width, bg_width):
            repeated_image.paste(image, (x, y))
    return repeated_image


class GameCanvas(tk.Canvas):
    UNIT = 70
    HOLE_SIZE = UNIT * 0.8
    HOLE_MARGIN = (HOLE_SIZE - UNIT) / 2
    PANEL_MARGIN = 10

    def __init__(self, master):
        self.game_frame = master
        self.game = master.game
        self.bg_image = Image.open("src/res/noise.png")
        self.bg_canvas = tk.Canvas(master, width=800, height=600, highlightthickness=0, bg="#7B4D62")

        self.canvas_window = None
        self.bg_canvas.pack(side=tk.BOTTOM, fill="both", expand=True)
        self.bg_canvas.bind("<Configure>", self.on_resize)

        super().__init__(self.bg_canvas, width=7 * self.UNIT + 2 * self.PANEL_MARGIN + 3,
                         height=7 * self.UNIT + 2 * self.PANEL_MARGIN + 3, highlightthickness=0)

        self.bind("<Motion>", self.on_mouse_move)
        self.bind("<Leave>", self.on_mouse_leave)
        self.bind("<Button-1>", self.on_mouse_click)
        
        self.arrow = tk.Canvas.create_line(0, 0, 0, 6 * self.UNIT, arrow=tk.LAST, fill='red')
        self.label = tk.Canvas.create_text(0, -20, text='', fill='red')

        self.create_widgets()

    def on_mouse_move(self, event):
        cell_size = self.UNIT
        column = event.x // cell_size
        cols = 7 ; rows = 6
        if 0 <= column < cols:
            self.bg_canvas.coords(self.arrow, column * cell_size + cell_size // 2, 0, 
                          column * cell_size + cell_size // 2, rows * cell_size)
            self.bg_canvas.coords(self.label, column * cell_size + cell_size // 2, -20)
            self.bg_canvas.itemconfig(self.label, text=f'Colonne {column + 1}')

    def on_mouse_leave(self, event):
        pass

    def on_mouse_click(self, event):
        x = (event.x - self.PANEL_MARGIN) // self.UNIT
        played = self.game_frame.player_play(x)
        if played is not None:
            self.add_token_animated(played[1], played[0], 1 if self.game.is_player_red else 2)
            self.after(500, self.computer_play)

    def computer_play(self):
        played = self.game_frame.computer_play()
        if played is not None:
            self.add_token_animated(played[1], played[0], 2 if self.game.is_player_red else 1)

    def add_token_animated(self, x, y, player, visible_y=0):
        if visible_y < y:
            self.set_token(x, y, player, visible_y=visible_y)

            self.after(20, lambda: self.add_token_animated(x, y, player, visible_y + 1))
            return

        self.set_token(x, y, player)

    def create_widgets(self):
        # Draw the board: 8ux7u blue rectangle, and 8ux7u white ovals to make holes in the board
        self.create_rectangle(1.5, 1.5+self.UNIT, 7 * self.UNIT + 2 * self.PANEL_MARGIN, 6 * self.UNIT + 2 * self.PANEL_MARGIN,
                              fill="#0029D9", outline="#506CE3", width=3)
        for x in range(7):
            for y in range(6):
                self.set_token(x, y, 0)

    def update_board(self):
        for x in range(7):
            for y in range(6):
                self.set_token(x, y, self.game.grid[y][x])

    def set_token(self, x, y, player, visible_y=-1):
        if len(self.find_withtag(f"token_{x}_{y}")) != 0:
            self.delete(f"token_{x}_{y}")

        if visible_y == -1:
            visible_y = y

        color = "red" if player == 1 else "yellow" if player == 2 else "white"
        self.create_oval(self.PANEL_MARGIN + x * self.UNIT - self.HOLE_MARGIN,
                         self.PANEL_MARGIN + visible_y * self.UNIT - self.HOLE_MARGIN,
                         self.PANEL_MARGIN + (x + 1) * self.UNIT + self.HOLE_MARGIN,
                         self.PANEL_MARGIN + (visible_y + 2) * self.UNIT + self.HOLE_MARGIN,
                         fill=color, outline="#506CE3", width=3,
                         tags="token_background" if player == 0 else f"token_{x}_{y}")

    def on_resize(self, event):
        self.setup_background(event.width, event.height)

    def setup_background(self, width, height):
        height = max(height - 5, 0)

        self.bg_canvas.config(width=width, height=height)
        repeated_image = create_repeated_image(self.bg_image, width, height)
        blurred_image = repeated_image.filter(ImageFilter.GaussianBlur(radius=0))
        overlay_color = (255, 255, 255, 200)
        overlay = Image.new('RGBA', blurred_image.size, overlay_color)
        combined_image = Image.alpha_composite(blurred_image.convert('RGBA'), overlay)

        self.bg_image_reference = ImageTk.PhotoImage(combined_image)
        self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_image_reference)

        center_x = width // 2
        center_y = height // 2
        if self.canvas_window is None:
            self.canvas_window = self.bg_canvas.create_window(center_x, center_y, window=self, anchor="center")
        else:
            self.bg_canvas.coords(self.canvas_window, center_x, center_y)
