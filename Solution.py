"""
Island Challenge
"""


import collections
import sys
from pathlib import Path
from collections import deque
import os


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
    largest_size = []
    results = []
    
    

    def bfs (r,c): 
            features = {
                "+": 0,
                "*": 0,
                "^": 0,
                "@": 0
            }
            size = 0
            queue = collections.deque()
            queue.append((r,c))
            visit.add((r,c))

            while queue:
                r,c = queue.popleft()
                size += 1
                features[grid[r][c]] += 1
                for dr, dc in Neighbours:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] in Landmass and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        queue.append((nr,nc))
            return size, features

    
    for r in range(height):
        for c in range(width):
            if grid[r][c] in Landmass and (r,c) not in visit:
                size, features = bfs(r,c)
                Landmasses += 1 
                largest_size.append(size)
                results.append((Landmasses, size, features))
              
    biggest_size = max(largest_size) if largest_size else 0
    return Landmasses , biggest_size , results

   
     
def main():
    if len(sys.argv) != 2:
        print("Usage: python Solution.py <map_file>")
        sys.exit(1)

    map_file = sys.argv[1]
    if not Path(map_file).is_file():
        print(f"Error: File '{map_file}' does not exist.")
        sys.exit(1)

    grid = read_map(map_file)
    landmass_count, biggest_size, results   = find_landmass(grid)


    print("#############################################")
    print("Reese Blackman: Island Challenge Report")
    print("#############################################\n")
    print(f"Total landmasses of {Path(map_file[:4])}: {landmass_count}")
    print(f"Largest landmass size: {biggest_size}\n")


    
    for landmass, size, features in results:
        print(f"Landmass {landmass} size: {size}")
        for feature, count in features.items():
            if count > 0:
                print(f"  {Feature_names[feature]}: {count}")
        print("\n")
    #os.startfile(map_file) # Opens the map only use on Windows OS



if __name__ == "__main__":
    main()



   



