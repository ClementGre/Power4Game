import tkinter as tk
from tkinter import ttk

bg = "#F5F3D1"


class ScoreboardFrame(tk.Frame):
    __slots__ = ["title_frame", "filter_frame", "player_name_entry", "difficulty_entry", "filter_button", "canvas",
                 "scrollbar", "scoreboard_frame", "scoreboard_frame_id", "widgets"]

    def __init__(self, master):
        """
        :type master: GameFrame
        """
        super().__init__(master, bg=bg)
        self.widgets = []

        self.create_widgets()

    def create_widgets(self):
        # Create a title frame to keep the title fixed
        self.title_frame = tk.Frame(self, bg=bg)
        self.title_frame.pack(side=tk.TOP, pady=10)

        title_label = tk.Label(self.title_frame, text="Scoreboard", bg=bg, font="Helvetica 19 bold", fg="#2D323B")
        title_label.pack()

        # Create filter fields
        self.filter_frame = tk.Frame(self, bg=bg)
        self.filter_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        tk.Label(self.filter_frame, text="Player Name:", bg=bg).grid(row=0, column=1, padx=5)
        self.player_name_entry = tk.Entry(self.filter_frame)
        self.player_name_entry.grid(row=0, column=2, padx=5)

        tk.Label(self.filter_frame, text="Difficulty:", bg=bg).grid(row=0, column=3, padx=5)
        self.difficulty_entry = tk.Entry(self.filter_frame)
        self.difficulty_entry.grid(row=0, column=4, padx=5)

        self.filter_button = tk.Button(self.filter_frame, text="Filter", command=self.update_scores)
        self.filter_button.grid(row=0, column=5, padx=5)

        # Center the filter fields
        tk.Frame(self.filter_frame, bg=bg).grid(row=0, column=0)
        tk.Frame(self.filter_frame, bg=bg).grid(row=0, column=6)
        self.filter_frame.grid_columnconfigure(0, weight=1)
        self.filter_frame.grid_columnconfigure(6, weight=1)

        # Create a canvas and scrollbar for the scoreboard
        self.canvas = tk.Canvas(self, bg=bg)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        self.scoreboard_frame = tk.Frame(self.canvas, bg=bg)
        self.scoreboard_frame_id = self.canvas.create_window((0, 0), window=self.scoreboard_frame, anchor="n")

        self.scoreboard_frame.grid_columnconfigure(0, weight=1)
        self.scoreboard_frame.grid_columnconfigure(8, weight=1)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        self.scoreboard_frame.bind("<Configure>", self.on_canvas_configure)

        self.draw_scores()

    def draw_scores(self, scores=None):
        for widget in self.widgets:
            widget.destroy()
        self.widgets = []

        if scores is None:
            scores = self.master.master.scoreboard.get_best_scores()

        if len(scores) == 0:
            label = tk.Label(self.scoreboard_frame, text="No scores found", bg=bg)
            label.grid(row=1, column=1, padx=2, pady=2)
            self.widgets.append(label)
            return

        headers = ["Player name", "Nb played", "Time", "Difficulty", "Score", "Date"]
        for col, header in enumerate(headers, start=1):
            label = tk.Label(self.scoreboard_frame, text=header, bg=bg)
            label.grid(row=0, column=col, padx=2, pady=2)
            self.widgets.append(label)

        for row, data in enumerate(scores, start=1):
            for col, cell in enumerate(data, start=1):
                label = tk.Label(self.scoreboard_frame, text=cell, bg=bg)
                label.grid(row=row, column=col, padx=2, pady=2)
                self.widgets.append(label)

    def update_scores(self):
        player_name = self.player_name_entry.get()
        difficulty = self.difficulty_entry.get()
        try:
            difficulty = int(difficulty)
        except (TypeError, ValueError):
            difficulty = None

        scores = self.master.master.scoreboard.get_best_scores(player_name=player_name or None,
                                                               difficulty=difficulty or None)
        self.draw_scores(scores=scores)

    def on_canvas_configure(self, event):
        # Update scroll region and ensure the canvas fills the entire parent frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfig(self.scoreboard_frame_id, width=self.canvas.winfo_width())

        height = self.winfo_height() - self.filter_frame.winfo_height() - self.title_frame.winfo_height()
        self.canvas.config(height=height)
