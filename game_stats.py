import json
import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        # Load the high score first
        self.high_score = self._load_high_score()
        # Then reset other stats
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1  # Start at level 1
        # Don't reset high_score here - it should persist between games

    def _load_high_score(self):
        """Load the high score from a file."""
        try:
            with open('high_score.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)

