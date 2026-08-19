""""
Island Challenge
"""


import collections
import sys
from pathlib import Path
from collections import deque

Landmass = {"+", "*", "^", "@"}

Feature_names = {
    "+": "land",
    "*": "tree",
    "^": "mountain",
    "@": "building",
}

Neighbours = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1), (-1, 1), (1, -1)]   

def read_map(file_path):
    """Reads a map from a file and returns it as a list of lists."""
    with open(file_path, "r") as f:
        return [list(line.strip()) for line in f.readlines()] 
    

def find_landmass(grid):
    
    height = len(grid)
    width = len(grid[0])

   
    visit = set()
    Landmasses = 0 

    def bfs (r,c): 
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r,c = queue.popleft()
                for dr, dc in Neighbours:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] in Landmass and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        queue.append((nr,nc))


    for r in range (height):
        for c in range(width):
        
            if grid[r][c] in Landmass and (r,c) not in visit:
                
                bfs(r,c)
                Landmasses += 1
    return Landmasses

def main():
    if len(sys.argv) != 2:
        print("Usage: python Solution.py <map_file>")
        sys.exit(1)

    map_file = sys.argv[1]
    if not Path(map_file).is_file():
        print(f"Error: File '{map_file}' does not exist.")
        sys.exit(1)

    grid = read_map(map_file)
    landmass_count = find_landmass(grid)
    print(f"Number of landmasses: {landmass_count}")



if __name__ == "__main__":
    main()



   



