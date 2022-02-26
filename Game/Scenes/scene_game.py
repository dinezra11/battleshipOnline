""" This is the code for the actual game (match) scene. The whole match logic and states are defined here.
    A match has 3 stages: Preparation, Fight, End.
        Preparation:    Each player need to place his/her ships on the board. When done, the player will press on a
                        'Ready' button, to indicates that the player is ready to fight.
                        When both of the players are ready, the game's state will be changed to 'Fight'.
        Fight:          Each player in his turn needs to guess the opponent's battleships' positions.
                        If there is a successful guess, the ship will sink.
                        The goal is to sink all of the opponent's ships.
        End:            The game ends when one player has no longer ships on his/her board.

    The boards are objects of the class Board. The size of the board is 10x10 cells.
    The class is responsible to draw the board, update the board during the game, highlight the appropriate area of the
    board according to the user's mouse position, and basically anything that is related to the board itself.

    The class 'SceneGame' is the class that defines the whole game's scene behaviour. It inherits from the base Scene
    class, and is used in 'main.py' to engage the scene. """
import pygame

from .scene import Scene


class Board:
    """ Board's class.
    Each object of this class is a player's board. The board will be 10x10 cells size, printed as a fixed table with
    10 columns and 10 rows. The ships will be drawn over the board. """

    def __init__(self, rect):
        """ Initialize the Board's object.

        :param rect:        Position and size of the board. (x, y, width, height)
        """
        self.rect = rect
        self.backgroundColor = (255, 255, 255)  # Board's background color -> White
        self.borderColor = (0, 0, 0)  # Board's borders color -> Black
        self.borderWidth = 2
        self.cellSize = (rect[2] / 10, rect[3] / 10)  # Calculate a board's single cell's size

        self.highlightSurface = pygame.Surface(
            (self.cellSize[0] - self.borderWidth, self.cellSize[1] - self.borderWidth))  # Surface of single cell's size
        self.highlightSurface.fill((255, 255, 0))  # Cell's highlighted color -> Yellow
        self.highlightSurface.set_alpha(150)  # Make the surface a bit transparent
        self.isHighlighted = False
        self.mousePos = None

    def update(self):
        """ Update the board. """
        self.mousePos = pygame.mouse.get_pos()

        # Toggle highlighted mode if needed.
        if (self.rect[0] < self.mousePos[0] < self.rect[0] + self.rect[2]) and (
                self.rect[1] < self.mousePos[1] < self.rect[1] + self.rect[3]):
            self.isHighlighted = True
        else:
            self.isHighlighted = False

    def draw(self, display: pygame.Surface):
        """ Draw the board. """
        pygame.draw.rect(display, self.backgroundColor, self.rect)

        # Draw cell's borders.
        x, y = self.rect[0], self.rect[1]
        for i in range(11):
            pygame.draw.line(display, self.borderColor, (x + i * self.cellSize[0], y),
                             (x + i * self.cellSize[0], y + self.rect[3]), self.borderWidth)
            pygame.draw.line(display, self.borderColor, (x, y + i * self.cellSize[1]),
                             (x + self.rect[2], y + i * self.cellSize[1]), self.borderWidth)

        # Highlight the cell, if needed.
        if self.isHighlighted:
            self.highlightCell(display, self.getCell(self.mousePos))

    def getCell(self, mousePos) -> tuple:
        """ Get the cell indices which the user's mouse is pointing at.

        :param mousePos:    The position of the mouse.
        :return:            A tuple that indicates the indices of a board's cell. (Starting from 0)
        """
        x, y = None, None
        for i in range(10):
            if self.rect[0] + i * self.cellSize[0] <= mousePos[0] < self.rect[0] + (i + 1) * self.cellSize[0]:
                x = i
            if self.rect[1] + i * self.cellSize[1] <= mousePos[1] < self.rect[1] + (i + 1) * self.cellSize[1]:
                y = i

            if (x is not None) and (y is not None):
                break  # Stop the loop if both x and y have been found

        return tuple((x, y))

    def highlightCell(self, display: pygame.Surface, cell: tuple):
        """ Highlight a given cell, by drawing the 'highlightSurface' on top of it.

        :param display:     The game screen's display, where to draw the surfaces.
        :param cell:        The indices of the cell in the 10x10 board. (Indices numbered 0..9)
        """
        display.blit(self.highlightSurface,
                     (self.rect[0] + cell[0] * self.cellSize[0] + self.borderWidth,
                      self.rect[1] + cell[1] * self.cellSize[1] + self.borderWidth))


class SceneGame(Scene):
    def __init__(self, display, *args):
        Scene.__init__(self, display, *args)
        self.board = Board((20, 20, 500, 500))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.board.update()

    def draw(self, display: pygame.Surface):
        display.fill((100, 100, 100))
        self.board.draw(display)
