import pygame
from constants import *
from player import Player


def main():
    # Initialize pygame at the beginning of your main() function
    pygame.init()
    print("Starting asteroids!")
    # Use pygame’s display.set_mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # create a new pygame.time.Clock object to help with FPS.
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    # Use an infinite while loop for the game loop
    while True:
        # This for loop will check if the user has closed the window and exit the game loop if they do.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Hook the update method into the game loop by calling it on the player object each frame before rendering.
        player.update(dt)
        # Use the screen’s fill method to fill the screen with a solid “black” color
        screen.fill("black")
        player.draw(screen)
        # Use pygame’s display.flip() method to refresh the screen.
        pygame.display.flip()
        # limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()