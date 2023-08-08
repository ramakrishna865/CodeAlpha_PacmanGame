import random

# Define the maze
maze = [
    "#####",
    "# P #",
    "#   #",
    "# G #",
    "#####"
]

# Initialize game variables
player_row = 1
player_col = 1
ghost_row = 3
ghost_col = 3
food_count = 0

# Main game loop
while True:
    # Print the maze
    for row in maze:
        print(row)
    
    # Get user input
    direction = input("Enter direction (w/a/s/d): ")
    
    # Update player position
    if direction == 'w':
        if maze[player_row - 1][player_col] != '#':
            player_row -= 1
    elif direction == 'a':
        if maze[player_row][player_col - 1] != '#':
            player_col -= 1
    elif direction == 's':
        if maze[player_row + 1][player_col] != '#':
            player_row += 1
    elif direction == 'd':
        if maze[player_row][player_col + 1] != '#':
            player_col += 1
    
    # Check for collisions
    if player_row == ghost_row and player_col == ghost_col:
        print("Game Over! You were caught by the ghost.")
        break
    
    if maze[player_row][player_col] == '.':
        maze[player_row] = maze[player_row][:player_col] + ' ' + maze[player_row][player_col + 1:]
        food_count += 1
        print(f"You ate {food_count} food")
    
    if food_count == 3:
        print("Congrwatulations! You won!")
        break
    
    # Update ghost position
    ghost_moves = ['w', 'a', 's', 'd']
    ghost_move = random.choice(ghost_moves)
    if ghost_move == 'w' and maze[ghost_row - 1][ghost_col] != '#':
        ghost_row -= 1
    elif ghost_move == 'a' and maze[ghost_row][ghost_col - 1] != '#':
        ghost_col -= 1
    elif ghost_move == 's' and maze[ghost_row + 1][ghost_col] != '#':
        ghost_row += 1
    elif ghost_move == 'd' and maze[ghost_row][ghost_col + 1] != '#':
        ghost_col += 1
