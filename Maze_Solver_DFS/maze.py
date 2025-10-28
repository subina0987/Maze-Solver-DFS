import tkinter as tk
from tkinter import messagebox
import random, time

ROWS, COLS = 10, 10
CELL_SIZE = 40
maze = []
start = (0, 0)
end = (ROWS - 1, COLS - 1)
speed = 0.1

root = tk.Tk()
root.title("AI Maze Solver using Depth-First Search (DFS)")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="Maze Solver using Depth-First Search (DFS)",
                       font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=10)

canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white", highlightthickness=0)
canvas.pack(pady=10)

def generate_maze():
    global maze
    maze = [[random.choice([0, 1, 0, 0]) for _ in range(COLS)] for _ in range(ROWS)]
    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0
    draw_maze()

def draw_maze():
    canvas.delete("all")
    for i in range(ROWS):
        for j in range(COLS):
            color = "white" if maze[i][j] == 0 else "#2c2c2c"
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE,
                                    (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                                    fill=color, outline="#3e3e3e")
    draw_cell(start[0], start[1], "#00bfff")
    draw_cell(end[0], end[1], "#32cd32")

def draw_cell(i, j, color):
    canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE,
                            (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE,
                            fill=color, outline="#3e3e3e")
    root.update()
    time.sleep(speed)

path = []

def is_valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] == 0

def dfs(x, y):
    if (x, y) == end:
        path.append((x, y))
        draw_cell(x, y, "#32cd32")
        return True
    if not is_valid(x, y):
        return False
    maze[x][y] = 2
    draw_cell(x, y, "#f4d03f")
    path.append((x, y))
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if dfs(x + dx, y + dy):
            return True
    draw_cell(x, y, "#e74c3c")
    path.pop()
    return False

def solve_maze():
    global path
    path.clear()
    draw_maze()
    for i in range(ROWS):
        for j in range(COLS):
            if maze[i][j] == 2:
                maze[i][j] = 0
    result = dfs(start[0], start[1])
    if result:
        messagebox.showinfo("Maze Solver", "✅ Path Found Successfully!")
    else:
        messagebox.showwarning("Maze Solver", "❌ No Path Found!")
    draw_maze()

def change_speed(val):
    global speed
    speed = float(val)

speed_label = tk.Label(root, text="Visualization Speed", font=("Arial", 11), bg="#1e1e1e", fg="white")
speed_label.pack(pady=(5, 0))

speed_slider = tk.Scale(root, from_=0.01, to=0.5, resolution=0.01, orient="horizontal",
                        length=200, command=change_speed, bg="#1e1e1e", fg="white", troughcolor="#2e2e2e")
speed_slider.set(speed)
speed_slider.pack(pady=5)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Generate Maze", command=generate_maze,
          font=("Arial", 12), bg="#0078d7", fg="white", width=14).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Solve Maze", command=solve_maze,
          font=("Arial", 12), bg="#28a745", fg="white", width=14).grid(row=0, column=1, padx=10)

generate_maze()
root.mainloop()