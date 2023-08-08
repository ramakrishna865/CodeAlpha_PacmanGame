import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Pacman properties
pacman_radius = 20
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Food properties
food_radius = 10
foods = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(10)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pacman based on arrow keys
    keys = pygame.key.get_pressed()
    pacman_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * pacman_speed
    pacman_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * pacman_speed

    # Check for collisions with food
    eaten_food = []
    for food in foods:
        food_x, food_y = food
        distance = ((food_x - pacman_x) ** 2 + (food_y - pacman_y) ** 2) ** 0.5
        if distance < pacman_radius + food_radius:
            eaten_food.append(food)

    for food in eaten_food:
        foods.remove(food)
        foods.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    # Clear the screen
    screen.fill(BLACK)

    # Draw Pacman
    pygame.draw.circle(screen, YELLOW, (int(pacman_x), int(pacman_y)), pacman_radius)

    # Draw food
    for food in foods:
        pygame.draw.circle(screen, YELLOW, food, food_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
