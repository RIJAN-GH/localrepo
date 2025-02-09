import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw a line using Bresenhams algorithm
def draw_line_bresen(x1, y1, x2, y2):

    x, y = x1, y1
    if x2 > x1:
        lx = 1
    else:
        lx = -1

    if y2 > y1:
        ly = 1
    else:
        ly = -1
     
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx > dy:
        p = 2 * dy - dx
        while x != x2:
            screen.set_at((x, y), WHITE)
            if p < 0:
                x = x + lx
                y = y
                p = p + 2 * dy
            else:
                x = x + lx
                y = y + ly
                p = p + 2 * dy - 2 * dx
    else:
        p = 2 * dx - dy
        while y != y2:
            screen.set_at((x, y), WHITE)
            if p < 0:
                y = y + ly
                x = x
                p = p + 2 * dx
            else:
                y = y + ly
                x = x + lx
                p = p + 2 * dx - 2 * dy

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using Bresenham's algorithm
        draw_line_bresen(400, 300, 300, 300)
        draw_line_bresen(300, 300, 350, 250)
        draw_line_bresen(350, 250, 450, 250)
        draw_line_bresen(450, 250, 400, 300)

        draw_line_bresen(400, 300, 400, 400)
        draw_line_bresen(400, 400, 450, 350)
        draw_line_bresen(450, 350, 450, 250)
        draw_line_bresen(400, 400, 300, 400)
        draw_line_bresen(300, 400, 300, 300)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
