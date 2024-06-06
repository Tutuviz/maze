import os
import time
import random
import argparse

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def createMaze(size, speed):
  maze = []
  for _ in range(size):
    maze.append(["⬛"] * size)

  maze[0][0] = "🟩"
  maze[size - 1][size - 1] = "🏁"

  def carve(x, y): 
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
      nx, ny = x + dx * 2, y + dy * 2

      if (0 <= nx < size and 0 <= ny < size and maze[nx][ny] == "🏁") or (0 <= x + dx < size and 0 <= y + dy < size and maze[x + dx][y + dy] == "🏁"):
        if (maze[len(maze) - 2][len(maze) - 1] == "🟦" or maze[len(maze) - 1][len(maze) - 2 ] == "🟦"):
          continue

      if 0 <= nx < size and 0 <= ny < size and (maze[nx][ny] == "⬛" or maze[nx][ny] == "🏁"):
        if maze[nx][ny] != "🏁":
          maze[nx][ny] = "🟦"
        if maze[x + dx][y + dy] != "🏁":
          maze[x + dx][y + dy] = "🟦"

        for i in range(len(maze)):
          print("".join(maze[i]))
        time.sleep(speed)

        clear()

        if maze[nx][ny] != "🏁" and maze[x + dx][y + dy] != "🏁":
          carve(nx, ny)

  carve(0, 0)

  return maze

def solveMaze(maze, start):
  rows = len(maze[0])
  cols = len(maze)
  path = []
  visited = []

  for _ in range(rows):
    visited.append([False] * cols)

  def search(x, y):
    # Check if x and y are within the maze
    # Check if the cell is already visited
    # Check if the cell is a wall
    if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y] or maze[x][y] == "⬛":
      return False
    
    if maze[x][y] == "🏁":
      path.append((x, y))
      return True
    
    visited[x][y] = True
    
    path.append((x, y))
    
    # Check if the path direction is valid
    if search(x - 1, y) or search(x, y + 1) or search(x + 1, y) or search(x, y - 1):
      return True
    
    # If the path is invalid, remove the cell from the path
    path.pop()
    return False

  search(start[0], start[1])

  return path

def printMazePath(maze, path, speed):
  for idx, step in enumerate(path):
    if idx + 1 < len(path) and idx != 0: maze[step[0]][step[1]] = '🟪'
    for i in range(len(maze)):
      print("".join(maze[i]))
    time.sleep(speed)
    if idx + 1 < len(path): clear()

parser = argparse.ArgumentParser(description='Transpile Python code and optionally run it.')

parser.add_argument('--size', help='size of the maze, max 51', required=True, type=int)

args = parser.parse_args()

size = args.size

if args.size > 51:
  print("Maze size must be less than 51, using 51 as default")
  size = 51

if size % 2 == 0:
  size += 1

speed = 0.01

if size > 25:
  speed = 0.001

maze = createMaze(size, speed)

clear()

for i in range(len(maze)):
  print("".join(maze[i]))

time.sleep(1)

clear()

start = [0, 0]

path = solveMaze(maze, start)

if not path:
  print("Labirinto fornecido não possui uma solução :(")
else:
  printMazePath(maze, path, speed * 10)

  print("Solução encontrada! :)")