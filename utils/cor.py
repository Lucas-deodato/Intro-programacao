"""
This module defines color codes for terminal output, 
  allowing for easy customization of text colors in console applications.
"""


class Cor:
    """
    Defines color codes for terminal output.

    Attributes:
        VERMELHO (str): Red color code.
        VERDE (str): Green color code.
        AMARELO (str): Yellow color code.
        AZUL (str): Blue color code.
        MAGENTA (str): Magenta color code.
        CIANO (str): Cyan color code.
        RESET (str): Reset color code.
    """

    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    RESET = "\033[0m"

    @staticmethod
    def get_color_code(color_name):
        """
        Returns the color code for the specified color name.

        Args:
            color_name (str): The name of the color.

        Returns:
            str: The color code corresponding to the color name.
        """
        colors = {
            "VERMELHO": Cor.VERMELHO,
            "VERDE": Cor.VERDE,
            "AMARELO": Cor.AMARELO,
            "AZUL": Cor.AZUL,
            "MAGENTA": Cor.MAGENTA,
            "CIANO": Cor.CIANO,
            "RESET": Cor.RESET,
        }
        return colors.get(color_name.upper(), "")

    @staticmethod
    def apply_multiple_colors(*colors):
        """
        Applies multiple colors sequentially.

        Args:
            *colors (list[str]): A list of color codes to apply sequentially.

        Returns:
            str: The concatenated string of color codes.
        """
        return "".join(colors) + Cor.RESET
