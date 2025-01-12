import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid point Circle Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw Circle using Mid-point algorithm
def Circle(radius, x_center, y_center):
    x = 0 
    y = radius
    p = 1 - radius

    def plot_points(cx, cy, x, y):
        # Plot the symmetrical points for all octants
        screen.set_at((cx + x, cy + y), WHITE) # Bottom right
        screen.set_at((cx - x, cy + y), WHITE) # Bottom left
        screen.set_at((cx + x, cy - y), WHITE) # Top right
        screen.set_at((cx - x, cy - y), WHITE) # Top left
        screen.set_at((cx + y, cy + x), WHITE) # Bottom-top right
        screen.set_at((cx - y, cy + x), WHITE) # Bottom top left
        screen.set_at((cx + y, cy - x), WHITE) # Top-Bottom right
        screen.set_at((cx - y, cy - x), WHITE) # Top-Bottom left

    plot_points(x_center, y_center, x, y)

    while x < y:
        if p <= 0:
            x += 1
            p += 2 * x + 1

        elif p > 0:
            x = x + 1
            y = y - 1
            p += (2 * x) - (2 * y) + 1


# Main loop 
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BLACK)

        # Draw a Circle Algorithm
        Circle(100, 400, 400)
        Circle(80, 400, 400)
        Circle(60, 400, 400)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
