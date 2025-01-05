import pygame
import sys
import math 

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)           # RGB for black
WHITE = (255, 255, 255)     # RGB for white
RED = (255, 0, 0)           # RGB for red
GREEN = (0, 255, 0)         # RGB for green
BLUE = (0, 0, 255)          # RGB for blue
YELLOW = (255, 255, 0)      # RGB for yellow
CYAN = (0, 255, 255)        # RGB for cyan
MAGENTA = (255, 0, 255)     # RGB for magenta
ORANGE = (255, 165, 0)      # RGB for orange
PINK = (255, 192, 203)      # RGB for pink
PURPLE = (128, 0, 128)
light_skin = (255, 224, 185)
GREY = (128, 128, 128)

# Function to draw a line
def draw_line(x1, y1, x2, y2, color):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 50)  # Line width is 5

# Function to draw a filled Circle using Pygame
def Circle(radius, x_center, y_center, color):
    pygame.draw.circle(screen, color, (x_center, y_center), radius)

# Function to draw a filled half Ellipse using Pygame
def ellipse(rx, ry, x_center, y_center, color):
    pygame.draw.ellipse(screen, color, (x_center - rx, y_center - ry, 2*rx, 2*ry))

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BLACK)

        # Draw filled Ellipses
        ellipse(150, 50, 200, 400, WHITE)
        ellipse(150, 50, 600, 400, WHITE)

        # Draw filled Circles
        Circle(50, 200, 400, CYAN)
        Circle(50, 600, 400, CYAN)
        Circle(25, 200, 400, BLACK)
        Circle(25, 600, 400, BLACK)
        Circle(5, 215, 390, WHITE)
        Circle(5, 615, 390, WHITE)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
