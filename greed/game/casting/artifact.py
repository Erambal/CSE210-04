from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point


class Artifact(Actor):
    """An artifact that is in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._message = ""

    def set_message(self, text):
        """Sets the message to display.
        
        Args:
            text (string): The text to display.
        """
        self._message = text
    def get_message(self):
        """Returns the message to display.
        
        Returns:
            string: The text to display.
        """
        return self._message
        
