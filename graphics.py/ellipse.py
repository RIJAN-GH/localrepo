import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
        ellipse(200, 75, WIDTH // 2, HEIGHT // 2)
        ellipse(100, 50, WIDTH // 2, HEIGHT // 2)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
