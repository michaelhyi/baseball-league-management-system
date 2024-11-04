import re


class PlayerNotFoundError(Exception):
    pass


height_pattern = r"^(?:(\d{1,2})'(\d{1,2})\"|\d{1,2}'\s*\d{1,2}\s*\"|(?:(\d{1,2})\s*feet\s*(\d{1,2})\s*inches))$"


class PlayerServiceUtil:
    @staticmethod
    def validate_data(**kwargs):
        for key, value in kwargs.items():
            if isinstance(value, str) and (value is None or len(value) == 0):
                raise ValueError(f"{key} must not be empty")
            if isinstance(value, int) and value <= 0:
                raise ValueError(f"{key} must be positive")

    @staticmethod
    def validate_height(height):
        if not re.match(height_pattern, height):
            raise ValueError("Height must match the following pattern: <ft>'<in>\"")
