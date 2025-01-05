import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Among Us")

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

# Function to draw Circle using Mid-point algorithm
def Circle(radius, x_center, y_center, half):
    x = 0 
    y = radius
    p = 1 - radius

        # Plot the symmetrical points for all octants
    if half == "top":
        def plot_points(cx, cy, x, y):
            # Top half
            screen.set_at((cx + x, cy - y), WHITE)  # Top-Right
            screen.set_at((cx - x, cy - y), WHITE)  # Top-Left
            screen.set_at((cx + y, cy - x), WHITE)  # Right-Top
            screen.set_at((cx - y, cy - x), WHITE)  # Left-Top


    elif half == "bottom":
        def plot_points(cx, cy, x, y):
            # Bottom half
            screen.set_at((cx + x, cy + y), WHITE)  # Bottom-Right
            screen.set_at((cx - x, cy + y), WHITE)  # Bottom-Left
            screen.set_at((cx + y, cy + x), WHITE)  # Right-Bottom
            screen.set_at((cx - y, cy + x), WHITE)  # Left-Bottom

    elif half == "left":
        def plot_points(cx, cy, x, y):
            # Left half
            screen.set_at((cx - x, cy + y), WHITE)  # Bottom-Left
            screen.set_at((cx - x, cy - y), WHITE)  # Top-Left
            screen.set_at((cx - y, cy + x), WHITE)  # Left-Bottom
            screen.set_at((cx - y, cy - x), WHITE)  # Left-Top
 
            
    elif half == "right":
        def plot_points(cx, cy, x, y):
            # Right half
            screen.set_at((cx + x, cy + y), WHITE)  # Bottom-Right
            screen.set_at((cx + x, cy - y), WHITE)  # Top-Right
            screen.set_at((cx + y, cy + x), WHITE)  # Right-Bottom
            screen.set_at((cx + y, cy - x), WHITE)  # Right-Top

    plot_points(x_center, y_center, x, y)

    while x < y:
        if p <= 0:
            x += 1
            p += 2 * x + 1

        elif p > 0:
            x = x + 1
            y = y - 1
            p += (2 * x) - (2 * y) + 1
        plot_points(x_center, y_center, x, y)

# Function to draw an ellipse using the Midpoint Algorithm
def ellipse(rx, ry, x_center, y_center):
    x = 0
    y = ry
    rx2 = rx**2
    ry2 = ry**2
    two_rx2 = 2 * rx2
    two_ry2 = 2 * ry2

    # Region 1
    p1 = ry2 - (rx2 * ry) + (rx2 / 4)

    def plot_points(cx, cy, x, y):
        # Plot the symmetrical points for all quadrants
        screen.set_at((cx + x, cy - y), WHITE)
        screen.set_at((cx - x, cy - y), WHITE)

    plot_points(x_center, y_center, x, y)

    while (two_ry2 * x) < (two_rx2 * y):  # Region 1
        x += 1
        if p1 < 0:
            p1 += two_ry2 * x + ry2
        else:
            y -= 1
            p1 += two_ry2 * x - two_rx2 * y + ry2
        plot_points(x_center, y_center, x, y)

    # Region 2
    p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
    while y > 0:
        y -= 1
        if p2 > 0:
            p2 -= two_rx2 * y + rx2
        else:
            x += 1
            p2 += two_ry2 * x - two_rx2 * y + rx2
        plot_points(x_center, y_center, x, y)

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
        # Left among
        draw_line_dda(300, 300, 300, 321)
        draw_line_dda(375, 321, 275, 321)
        draw_line_dda(275, 391, 375, 391)
        draw_line_dda(300, 391, 300, 500)

        draw_line_dda(375, 500, 375, 450)
        draw_line_dda(375, 450, 340, 440)
        draw_line_dda(375, 450, 425, 465)
        draw_line_dda(425, 465, 425, 500)
    
        # Right among
        draw_line_dda(500, 500, 500, 300)
        draw_line_dda(500, 460, 530, 440)
        draw_line_dda(500, 325, 530, 345)
        draw_line_dda(530, 440, 530, 345)

        # Ellip
        ellipse(100, 75, 400, 300)
        
        # Cir
        Circle(37, 337, 500, "bottom")
        Circle(37, 462, 500, "bottom")

        Circle(35, 275, 356, "left")
        Circle(35, 375, 356, "right")
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
