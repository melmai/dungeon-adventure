from maze import Room
import random

class Dungeon:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.entrance_row = random.randint(0, self.rows - 1)
        self.entrance_col = random.randint(0, self.cols - 1)
        self.item_spawn_chance = 0.1
        self.rooms = []
        for i in range(rows):
            self.rooms.append([])
            for j in range(cols):
                self.rooms[-1].append(Room(i, j))

    def print(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.rooms[row][col], sep=' ', end="")
            print()

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.rooms[row][col].draw_top()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_middle()
            print()
            for col in range(self.cols):
                self.rooms[row][col].draw_bottom()
            print()

    def get_neighbors(self, current, visited):
        neighbors = []
        if current.row > 0 and not self.rooms[current.row - 1][current.col] in visited:  # check if we can go north
            neighbors.append(self.rooms[current.row - 1][current.col])
        if current.row < self.rows - 1 and not self.rooms[current.row + 1][current.col] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row + 1][current.col])
        if current.col > 0 and not self.rooms[current.row][current.col - 1] in visited:  # check if we can go west
            neighbors.append(self.rooms[current.row][current.col - 1])
        if current.col < self.cols - 1 and not self.rooms[current.row][current.col + 1] in visited:  # check if we can go south
            neighbors.append(self.rooms[current.row][current.col + 1])
        return neighbors

    def create_doors(self, current, neighbor):
        if neighbor.col - current.col > 0:
            current.east = True
            neighbor.west = True
        elif neighbor.col - current.col < 0:
            current.west = True
            neighbor.east = True
        elif neighbor.row - current.row > 0:
            current.south = True
            neighbor.north = True
        elif neighbor.row - current.row < 0:
            current.north = True
            neighbor.south = True

    def generate(self):
        source = self.rooms[self.entrance_row][self.entrance_col]
        stack = []
        visited = []
        stack.append(source)
        visited.append(source)
        while len(stack) != 0:
            current = stack[-1]
            neighbors = self.get_neighbors(current, visited)
            if len(neighbors) != 0:
                neighbor = random.choice(neighbors)
                visited.append(neighbor)
                stack.append(neighbor)
                self.create_doors(current, neighbor)
            else:
                stack.pop()
    
    def fill_rooms(self):
        self.rooms[self.entrance_row][self.entrance_col].entrance = True
        choices = []
        for row in range(self.rows):
            for col in range(self.cols):
                choices.append((row,col))
        choices.remove((self.entrance_row, self.entrance_col))
        exit_row_col = random.choice(choices)
        self.rooms[exit_row_col[0]][exit_row_col[1]].exit = True
        choices.remove(exit_row_col)
        pillar_rows_cols = []
        for i in range(0, 4):
            pillar_rows_cols.append(random.choice(choices))
            choices.remove(pillar_rows_cols[i])
        self.rooms[pillar_rows_cols[0][0]][pillar_rows_cols[0][1]].abstraction = True
        self.rooms[pillar_rows_cols[1][0]][pillar_rows_cols[1][1]].encapsulation = True
        self.rooms[pillar_rows_cols[2][0]][pillar_rows_cols[2][1]].inheritance = True
        self.rooms[pillar_rows_cols[3][0]][pillar_rows_cols[3][1]].polymorphism = True
        item_chance = [1 - self.item_spawn_chance, self.item_spawn_chance]
        items = ["Healing", "Vision", "Pit"]
        item_hit = ["No Item", "Item"]
        for item in items:
            for choice in choices:
                item_success = random.choices(item_hit, item_chance)
                if item_success == ["Item"]:
                    if item == "Healing":
                        self.rooms[choice[0]][choice[1]].healing_potion = True
                    elif item == "Vision":
                        self.rooms[choice[0]][choice[1]].vision_potion = True
                    elif item == "Pit":
                        self.rooms[choice[0]][choice[1]].pit = True
   