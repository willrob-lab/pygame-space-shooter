class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's  static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # black background
        
        # Ship settings
        self.ship_speed = 12
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)  # Red bullets
        
        # Alien settings
        self.fleet_drop_speed = 10  
        self.alien_points = 50  # Points for hitting an alien

        # How quickly the game speeds up
        self.speedup_scale = 2.2
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 12.0
        self.bullet_speed = 10.0
        self.alien_speed = 2.0

        #Scoring settings
        self.alien_points = 10

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
 
    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed += 1.0  # Increase bullet speed by 1.0 each level
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
