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

    def draw(self):
        """Draws the entire Dungeon"""
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
        """When generating dungeon this method checks for neighboring rooms"""
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
        """Creates a doorway between rooms when generating dungeon"""
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
        """Primary method to construct the dungeon"""
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
        """From the generated maze places entrance, exit, pillars, and items"""
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
    
    def vision_potion(self):
        """When player uses a vision potion this method will display the player room and all surrounding rooms."""
        player_location = [self.entrance_row, self.entrance_col] #place holder until it can access player location from adventurer class
        vision_rooms_row = player_location[0]
        vision_rooms_col = player_location[1]
        #case if player can see all 8 rooms
        if (vision_rooms_row > 0 and vision_rooms_row < self.rows - 1) and (vision_rooms_col > 0 and vision_rooms_col < self.cols - 1):
            for row in range(vision_rooms_row - 1, vision_rooms_row + 2):
                for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                    self.rooms[row][col].draw_top()
                print()
                for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                    self.rooms[row][col].draw_middle()
                print()
                for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                    self.rooms[row][col].draw_bottom()
                print()
        #cases if player on edge or corner
        elif (vision_rooms_row == 0 or vision_rooms_row == self.rows - 1) or (vision_rooms_col == 0 or vision_rooms_col == self.cols - 1):
            #dungeon corner cases
            if (vision_rooms_row == 0 or vision_rooms_row == self.rows - 1) and (vision_rooms_col == 0 or vision_rooms_col == self.cols - 1):
                if vision_rooms_row == 0 and vision_rooms_col == 0:
                    for row in range(vision_rooms_row, vision_rooms_row + 2):
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_bottom()
                        print()
                elif vision_rooms_row == 0 and vision_rooms_col == self.cols - 1:
                    for row in range(vision_rooms_row, vision_rooms_row + 2):
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_bottom()
                        print()
                elif vision_rooms_row == self.rows - 1 and vision_rooms_col == 0:
                    for row in range(vision_rooms_row - 1, vision_rooms_row + 1):
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_bottom()
                        print()
                else:
                    for row in range(vision_rooms_row - 1, vision_rooms_row + 1):
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_bottom()
                        print()
            else:
                #dungeon edge cases
                if vision_rooms_row == 0:
                    for row in range(vision_rooms_row, vision_rooms_row + 2):
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_bottom()
                        print()
                elif vision_rooms_row == self.rows - 1:
                    for row in range(vision_rooms_row - 1, vision_rooms_row + 1):
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 2):
                            self.rooms[row][col].draw_bottom()
                        print()
                elif vision_rooms_col == 0:
                    for row in range(vision_rooms_row - 1, vision_rooms_row + 2):
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col, vision_rooms_col + 2):
                            self.rooms[row][col].draw_bottom()
                        print()
                else:
                    for row in range(vision_rooms_row - 1, vision_rooms_row + 2):
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_top()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_middle()
                        print()
                        for col in range(vision_rooms_col - 1, vision_rooms_col + 1):
                            self.rooms[row][col].draw_bottom()
                        print()
