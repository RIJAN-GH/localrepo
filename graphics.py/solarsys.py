import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)           # RGB for black
WHITE = (255, 255, 255)     # RGB for white
ORANGE = (255, 165, 0)  
MERCURY = (169, 169, 169)    
VENUS = (237, 201, 175)
EARTH = (0, 102, 204)
MARS = (210, 105, 30)
JUPITER = (233, 196, 106)
SATURN = (255, 223, 186)
URANUS = (173, 216, 230)
NEPTUNE = (0, 0, 139)

# Function to draw an ellipse using the Midpoint Algorithm
def draw_ellipse(rx, ry, x_center, y_center):
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
        screen.set_at((cx + x, cy + y), WHITE)
        screen.set_at((cx - x, cy + y), WHITE)
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

# Function to draw Circle
def draw_circle(radius, x_center, y_center, color):
    pygame.draw.circle(screen, color, (x_center, y_center), radius)

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw an ellipse
        
        draw_ellipse(100, 60, 500, 400)
        draw_ellipse(150, 100, 500, 400)
        draw_ellipse(200, 140, 500, 400)
        draw_ellipse(250, 180, 500, 400)
        draw_ellipse(300, 220, 500, 400)
        draw_ellipse(350, 260, 500, 400)
        draw_ellipse(400, 300, 500, 400)
        draw_ellipse(450, 340, 500, 400)

        # Draw the Circle
        draw_circle(60, 500, 380, ORANGE)

        draw_circle(15, 600, 390, MERCURY)
        draw_circle(20, 365, 360, VENUS)
        draw_circle(24, 695, 425, EARTH)
        draw_circle(25, 300, 500, MARS)
        draw_circle(35, 625, 600, JUPITER)
        draw_circle(32, 350, 165, SATURN)
        draw_circle(27, 625, 120, URANUS)
        draw_circle(33, 50, 380, NEPTUNE)


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
