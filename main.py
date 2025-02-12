# import pygame at the top of your main.py file.
import pygame
# Ensure our predefined constants (constants.py) SCREEN_WIDTH and SCREEN_HEIGHT are imported at the top of your file
from constants import *

def main():
    # Initialize pygame at the beginning of your main() function
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Use pygame’s display.set_mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Use an infinite while loop for the game loop
    while True:
        # This for loop will check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Use the screen’s fill method to fill the screen with a solid “black” color
        screen.fill((0, 0, 0))
        # Use pygame’s display.flip() method to refresh the screen.
        pygame.display.flip()


if __name__ == "__main__":
    main()