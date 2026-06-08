class GameStats:
    """Track alien invasion stats"""

    def __init__(self,ai_game):
        """Init the stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats that change durring game"""
        self.ships_left = self.settings.ship_limit