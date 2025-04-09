# path_finder

#  A* Pathfinding Visualizer (Pygame)

This is a simple graphical Python application that demonstrates the A* pathfinding algorithm using the **Pygame** library. It allows users to interactively create a grid, place barriers, set start and end points, and visualize how the A* algorithm finds the shortest path.

---



##  Features

- Interactive grid interface
- Left-click to:
  - Place the **start** node (🟧 Orange)
  - Place the **end** node (🟦 Turquoise)
  - Place **barriers** (⬛ Black)
- Right-click to:
  - Remove any node or reset a position
- Press `SPACE` to:
  - Start the A* pathfinding algorithm
- Color-coded visualization:
  - **Green (🟩)**: Open nodes
  - **Red (🟥)**: Closed nodes
  - **Purple (🟪)**: Final shortest path

---

#  Requirements

- Python 3.x
- Pygame

Install Pygame using pip:

```bash
pip install pygame
