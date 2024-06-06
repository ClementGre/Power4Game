import tkinter as tk

from PIL import Image, ImageTk, ImageFilter


def create_repeated_image(image, width, height):
    """
    Crée une image répétée pour couvrir une zone donnée.

    :param image: L'image source à répéter.
    :type image: PIL.Image.Image
    :param width: La largeur de la zone à couvrir.
    :type width: int
    :param height: La hauteur de la zone à couvrir.
    :type height: int
    :return: L'image répétée couvrant la zone spécifiée.
    :rtype: PIL.Image.Image
    """
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
        self.bg_canvas = tk.Canvas(master, width=700, height=700, highlightthickness=0, bg="#7B4D62")

        self.canvas_window = None
        self.bg_canvas.pack(side=tk.BOTTOM, fill="both", expand=True)
        self.bg_canvas.bind("<Configure>", self.on_resize)

        super().__init__(self.bg_canvas, width=7 * self.UNIT + 2 * self.PANEL_MARGIN + 3,
                         height=6 * self.UNIT + 2 * self.PANEL_MARGIN + 3, highlightthickness=0)

        self.circle = self.create_oval(0, 0, 0, 0, fill='black')

        self.bind("<Motion>", self.on_mouse_move)
        self.bind("<Leave>", self.on_mouse_leave)
        self.bind("<Button-1>", self.on_mouse_click)

        # self.arrow = tk.Canvas.create_line(0, 0, 0, 6 * self.UNIT, arrow=tk.LAST, fill='red')
        # self.label = tk.Canvas.create_text(0, -20, text='', fill='red')

        self.create_widgets()

    def on_mouse_move(self, event):
        """
        Gère le mouvement de la souris sur le canevas du jeu.

        :param event: L'événement de mouvement de la souris.
        :type event: tk.Event
        """
        # Calculer la colonne sur laquelle la souris se trouve
        col = event.x // self.UNIT
        if 0 <= col < 7:
            # Calculer les coordonnées du cercle
            x1 = col * self.UNIT + self.PANEL_MARGIN + self.UNIT // 2 - 15
            y1 = 10
            x2 = col * self.UNIT + self.PANEL_MARGIN + self.UNIT // 2 + 15
            y2 = 40

            # Mettre à jour la position du cercle
            self.coords(self.circle, x1, y1, x2, y2)

    def on_mouse_leave(self, event):
        """
        Cache le cercle lorsque la souris quitte le canevas.

        :param event: L'événement de départ de la souris.
        :type event: tk.Event
        """
        self.coords(self.circle, 0, 0, 0, 0)

    def on_mouse_click(self, event):
        """
        Gère le clic de la souris sur le canevas du jeu.

        :param event: L'événement de clic de la souris.
        :type event: tk.Event
        """
        x = (event.x - self.PANEL_MARGIN) // self.UNIT
        played = self.game_frame.player_play(x)
        if played is not None:
            self.add_token_animated(played[1], played[0], 1 if self.game.is_player_red else 2)
            self.after(500, self.computer_play)

    def computer_play(self):
        """
        Gère le tour de jeu de l'ordinateur.
        """
        played = self.game_frame.computer_play()
        if played is not None:
            self.add_token_animated(played[1], played[0], 2 if self.game.is_player_red else 1)

    def add_token_animated(self, x, y, player, visible_y=0):
        """
        Ajoute un jeton au canevas de jeu avec une animation.

        :param x: La position x du jeton.
        :type x: int
        :param y: La position y du jeton.
        :type y: int
        :param player: Le numéro du joueur (1 ou 2).
        :type player: int
        :param visible_y: La position y visible pour l'animation (défaut est 0).
        :type visible_y: int
        """
        if visible_y < y:
            self.set_token(x, y, player, visible_y=visible_y)
            self.after(20, lambda: self.add_token_animated(x, y, player, visible_y + 1))
            return
        self.set_token(x, y, player)

    def create_widgets(self):
        """
        Crée et dessine les widgets du canevas de jeu.

        Dessine le plateau de jeu avec un rectangle bleu et des ovales blancs pour représenter les trous.
        """
        self.create_rectangle(1.5, 1.5, 7 * self.UNIT + 2 * self.PANEL_MARGIN, 6 * self.UNIT + 2 * self.PANEL_MARGIN,
                              fill="#0029D9", outline="#506CE3", width=3)
        for x in range(7):
            for y in range(6):
                self.set_token(x, y, 0)

    def update_board(self):
        """
        Met à jour l'affichage du plateau de jeu en fonction de l'état actuel de la grille.
        """
        for x in range(7):
            for y in range(6):
                self.set_token(x, y, self.game.grid[y][x])

    def set_token(self, x, y, player, visible_y=-1):
        """
        Définit un jeton sur le canevas de jeu.

        :param x: La position x du jeton.
        :type x: int
        :param y: La position y du jeton.
        :type y: int
        :param player: Le numéro du joueur (1 ou 2).
        :type player: int
        :param visible_y: La position y visible pour l'animation (défaut est -1).
        :type visible_y: int
        """
        if len(self.find_withtag(f"token_{x}_{y}")) != 0:
            self.delete(f"token_{x}_{y}")

        if visible_y == -1:
            visible_y = y

        color = "red" if player == 1 else "yellow" if player == 2 else "white"
        self.create_oval(self.PANEL_MARGIN + x * self.UNIT - self.HOLE_MARGIN,
                         self.PANEL_MARGIN + visible_y * self.UNIT - self.HOLE_MARGIN,
                         self.PANEL_MARGIN + (x + 1) * self.UNIT + self.HOLE_MARGIN,
                         self.PANEL_MARGIN + (visible_y + 1) * self.UNIT + self.HOLE_MARGIN,
                         fill=color, outline="#506CE3", width=3,
                         tags="token_background" if player == 0 else f"token_{x}_{y}")

    def on_resize(self, event):
        """
        Gère le redimensionnement du canevas de fond.

        :param event: L'événement de redimensionnement.
        :type event: tk.Event
        """
        self.setup_background(event.width, event.height)

    def setup_background(self, width, height):
        """
        Configure l'arrière-plan du canevas avec une image répétée.

        :param width: La nouvelle largeur du canevas.
        :type width: int
        :param height: La nouvelle hauteur du canevas.
        :type height: int
        """
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
