import pygame
import math
from queue import PriorityQueue

# Set up the game display window
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithm using A*")

#create colors for the grid
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Create a node class to represent each square in the grid

class Node:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width #coordinates that the square will be drawn
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    # Get the position of the nodes in the grid
    def get_position(self):
        return self.row, self.col
    
    #define different node states based on color
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE


    # Set node states based on the definitions above
    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK
    
    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color =TURQUOISE
    
    def make_path(self):
        self.color = PURPLE

    # Draw the node
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    
    # Update the neighbors of the node
    def update_neighbors(self, grid):
       pass
    
    # Define the less than function
    def __lt__(self, other):
        return False
    
# Define the heuristic function
def h(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
    
# Make the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows #width of each square is calculated by dividing the width of the grid by the number of rows 
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)
    return grid
    
#drawings the grid lines
def draw_grid_lines(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, width))
    
# draw
def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
        
    draw_grid_lines(window, rows, width)
    pygame.display.update()
     

# Get the clicked position
def get_click_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

# Main function
def main(WINDOW, WIDTH):
    ROWS = 50
    grid = make_grid(ROWS, WIDTH)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(WINDOW, grid, ROWS, WIDTH)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_click_pos(pos, ROWS, WIDTH)
                node = grid[row][col]

                if not start:
                    start = node
                    start.make_start()

                elif not end:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()


            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()
 
main(WINDOW, WIDTH)