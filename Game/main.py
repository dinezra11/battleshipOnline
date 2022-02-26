""" This file is the main python code for the client. All of the initial game's configurations will be defined here.
    This file is in charge of updating and drawing the current scene, navigating between the different scenes and
    basically call and apply all of the game's functions.

    Run this script if you want to run the game as a client. (To run the server, go to 'server.py' file in 'Server'
    directory)

    All of the game is programming in python using 'PyGame', 'threading' and 'sockets' libraries.
    Don't forget to install PyGame using 'pip install pygame' if you want to debug the code. The other libraries are
    built-in.

    Game was programmed by Din Ezra. You are very welcome to visit my GitHub or LinkedIn pages. :)
    Thanks for reviewing my code. Any comment or suggestion will be very appreciated.
"""
import pygame

import Scenes.scene as scene
from Scenes.scene_game import SceneGame

# Window Configurations
WIN_SIZE = (800, 600)
WIN_CAPTION = "Battleship Online - by Din Ezra"

# Scenes Dictionary (a dictionary of pointers to the scene's classes)
SCENES = {
    scene.SCENE_GAME: SceneGame
}


def main():
    """ Main function of the game. """
    def changeScene(newScene="", *args):
        """ Change the current screen to the desired one.
        End the game if newScene='endGame'.
        Do nothing if the desired scene doesn't exist in SCENES's dictionary.
        """
        nonlocal currentScene
        fadeSurface = pygame.Surface(gameDisplay.get_size())
        fadeSurface.fill((0, 0, 0))

        def fadeOut():
            for i in range(0, 255, 10):
                currentScene.draw(gameDisplay)
                fadeSurface.set_alpha(i)
                gameDisplay.blit(fadeSurface, (0, 0))
                pygame.display.update()
                gameClock.tick(60)

        def fadeIn():
            for i in range(255, 0, -10):
                currentScene.draw(gameDisplay)
                fadeSurface.set_alpha(i)
                gameDisplay.blit(fadeSurface, (0, 0))
                pygame.display.update()
                gameClock.tick(60)

        if newScene == "endGame":
            # Only fade out, to close the game
            fadeOut()
        elif newScene in SCENES:
            # Fade out and in to the new scene:
            fadeOut()
            del currentScene
            currentScene = SCENES[newScene](gameDisplay, args)
            fadeIn()

    def update():
        """ Update the screen according to the current scene. End the game when need to quit the game completely. """
        result = currentScene.update()
        if result is False:
            changeScene("endGame")
            return False

        return True  # Continue with the game's loop

    # Initialize PyGame and the screen's display:
    pygame.init()
    gameDisplay = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption(WIN_CAPTION)
    gameClock = pygame.time.Clock()

    currentScene = SCENES[scene.SCENE_GAME](gameDisplay) # This variable will hold the object of the current scene!

    # Game's Loop:
    while update():
        """ Draw the current scene. """
        currentScene.draw(gameDisplay)
        pygame.display.update()

        gameClock.tick(30)  # 30 FPS

    # Close PyGame safely and quit the game:
    pygame.quit()


if __name__ == '__main__':
    main()
