import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw a line using DDA algorithm
def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # If the line is a single point, just draw that point
    if dx == 0 and dy == 0:
        screen.set_at((x1, y1), WHITE)
        return
    
    # Determine the number of steps
    step = max(abs(dx), abs(dy))

    # Calculate increments
    xinc = dx / step
    yinc = dy / step

    # Initialize starting point
    x, y = x1, y1   

    # Draw the line pixel by pixel
    for i in range(step):
        screen.set_at((round(x), round(y)), WHITE)
        x += xinc
        y += yinc

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_dda(400, 100, 500, 200)
        draw_line_dda(400, 100, 300, 200)
        draw_line_dda(300, 200, 500, 200)
        
        draw_line_dda(300, 200, 300, 400)
        draw_line_dda(500, 200, 500, 400)
        draw_line_dda(300, 400, 500, 400)

        draw_line_dda(350, 300, 350, 400)
        draw_line_dda(450, 300, 450, 400)
        draw_line_dda(350, 300, 450, 300)

        draw_line_dda(375, 275, 425, 275)
        draw_line_dda(375, 225, 425, 225)

        draw_line_dda(375, 275, 375, 225)
        draw_line_dda(425, 275, 425, 225)


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
