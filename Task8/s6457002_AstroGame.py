#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
asteroid_evader.py
==================
Astronomy-themed asteroid evasion game for a university project.
Requires: pip install pygame

Controls:
  A / D arrow keys         →  move the spaceship
  R                        →  restart after Game Over
  ESC                      →  quit game
"""

import pygame
import random
import sys
import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCREEN_W, SCREEN_H = 800, 600
FPS = 60
FONT_SIZE = 22

# Each level defines a celestial body and its real gravitational acceleration
# (m/s²).  We scale g by GRAVITY_SCALE so the on-screen fall feels playable
# while still preserving the relative differences between bodies.
GRAVITY_SCALE = 8          # pixels-per-second² per 1 m/s² of real gravity
LEVELS = [
    {"name": "Moon",    "g": 1.62,  "color": (200, 200, 210), "bg": (10, 10, 30)},
    {"name": "Earth",   "g": 9.81,  "color": (100, 180, 100), "bg": (5,  20, 50)},
    {"name": "Neptune", "g": 11.15, "color": (80,  120, 200), "bg": (0,  10, 40)},
    {"name": "Jupiter", "g": 24.79, "color": (210, 160,  80), "bg": (20, 10, 10)},
]

# Difficulty ramps: how many asteroids spawn per second at each level
SPAWN_RATES = [1, 2, 4, 8]   # asteroids / second (index matches LEVELS)

# Score needed to advance to the next level
TIME_PER_LEVEL = 15


# ---------------------------------------------------------------------------
# Spaceship class
# ---------------------------------------------------------------------------
class Spaceship:
    """Represents the player-controlled spaceship at the bottom of the screen."""

    WIDTH  = 50
    HEIGHT = 30
    SPEED  = 4   # pixels per frame

    def __init__(self):
        """Initialise the ship centred horizontally near the bottom."""
        self.x = SCREEN_W // 2 - self.WIDTH // 2
        self.y = SCREEN_H - self.HEIGHT - 10
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    def move(self, keys):
        """Update horizontal position based on keyboard input.

        Args:
            keys: result of pygame.key.get_pressed()
        """
        if keys[pygame.K_a]  and self.rect.left  > 0:
            self.rect.x -= self.SPEED
        if keys[pygame.K_d] and self.rect.right < SCREEN_W:
            self.rect.x += self.SPEED

    def draw(self, surface):
        """Draw a layered cartoon spaceship."""
        r = self.rect
    
        # 1. Define the Wing Shape (A wider base triangle)
        # This sits behind the main body
        wings_points = [
            (r.centerx, r.top + 5),    # Slightly below the nose
            (r.left, r.bottom),        # Far left
            (r.right, r.bottom)        # Far right
        ]
        pygame.draw.polygon(surface, (0, 150, 200), wings_points) # Darker Blue
    
        # 2. Define the Main Fuselage (The central "rocket" body)
        # We make this narrower than the wings to create a 'stepped' look
        body_width = r.width * 0.6
        body_points = [
            (r.centerx, r.top),                    # Sharp Nose
            (r.centerx - body_width//2, r.bottom), # Bottom Left of body
            (r.centerx + body_width//2, r.bottom)  # Bottom Right of body
        ]
        pygame.draw.polygon(surface, (0, 220, 255), body_points) # Bright Blue
    
        # 3. Add a Cockpit/Window
        # A small circle or oval near the top
        cockpit_pos = (r.centerx, r.top + r.height // 3)
        pygame.draw.circle(surface, (200, 255, 255), cockpit_pos, 4)
    
        # 4. Engine Glow (Multi-layered for a "hotter" look)
        # Large outer orange glow
        pygame.draw.circle(surface, (255, 140, 0), r.midbottom, 8)
        # Small inner yellow core
        pygame.draw.circle(surface, (255, 255, 0), r.midbottom, 4)


# ---------------------------------------------------------------------------
# Asteroid class
# ---------------------------------------------------------------------------
class Asteroid:
    """A single falling asteroid whose speed increases under gravity."""

    MIN_RADIUS = 10
    MAX_RADIUS = 50

    def __init__(self, gravity_px: float):
        """Spawn the asteroid at a random horizontal position at the top.

        Args:
            gravity_px: gravitational acceleration in pixels/s² (already scaled).
        """
        self.radius = random.randint(15, 40)
        self.x = random.randint(self.radius, SCREEN_W - self.radius)
        self.y = -self.radius               # start just above the screen
        self.vy = random.uniform(60, 130)   # pixels / second
        self.gravity = gravity_px           # pixels / second^2

        self.color = (random.randint(100, 140),
                      random.randint(70, 100),
                      random.randint(60,  70)) 
        
        # Create a "jagged" shape by picking 8-12 points around a circle
        self.points = []
        num_points = random.randint(8, 12)
        for i in range(num_points):
            angle = (i / num_points) * 2 * 3.14159 # 360 degrees in radians
            # Vary the distance from the center slightly for each point
            dist = self.radius * random.uniform(0.7, 1.1)
            px = math.cos(angle) * dist
            py = math.sin(angle) * dist
            self.points.append((px, py))

    def update(self, dt: float):
        """Apply gravitational acceleration and move down by one time-step.

        Args:
            dt: elapsed time since last frame in seconds.
        """
        self.vy += self.gravity * dt   # v = v₀ + g·t  (Newtonian kinematics)
        self.y  += self.vy    * dt     # y = y₀ + v·t

    @property
    def rect(self) -> pygame.Rect:
        """Return a bounding Rect used for collision detection."""
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                           self.radius * 2,       self.radius * 2)

    def is_off_screen(self) -> bool:
        """Return True once the asteroid has fallen below the visible area."""
        return self.y - self.radius > SCREEN_H

    def draw(self, surface):
        """Draw the asteroid as a jagged polygon."""
        # Calculate the actual screen positions for the points
        screen_points = [(int(self.x + px), int(self.y + py)) for px, py in self.points]
        
        # Draw the rock body
        pygame.draw.polygon(surface, self.color, screen_points)
        # Draw a darker outline to make it pop
        pygame.draw.polygon(surface, (50, 50, 50), screen_points, 2)


# ---------------------------------------------------------------------------
# Game class
# ---------------------------------------------------------------------------
class Game:
    """Manages the main game loop, level progression, and rendering."""

    def __init__(self):
        """Initialise pygame, create the window, and reset game state."""
        pygame.init()
        self.screen  = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Asteroid Evader – Gravity Edition")
        self.clock   = pygame.font.SysFont(None, FONT_SIZE)   # HUD font
        self.ticker  = pygame.time.Clock()
        self.reset()

    def reset(self):
        """Reset all game state to start a fresh game from level 0."""
        self.level_index  = 0
        self.score        = 0.0          # accumulates over time (points/s)
        self.asteroids    = []
        self.spawn_timer  = 0.0          # seconds since last spawn
        self.ship         = Spaceship()
        self.game_over    = False

    # ------------------------------------------------------------------
    # Properties that read from the current level dict
    # ------------------------------------------------------------------
    @property
    def current_level(self) -> dict:
        """Return the dict describing the current celestial body."""
        return LEVELS[self.level_index]

    @property
    def gravity_px(self) -> float:
        """Real g (m/s²) scaled to pixels/s² for use in physics."""
        return self.current_level["g"] * GRAVITY_SCALE

    # ------------------------------------------------------------------
    # Core loop helpers
    # ------------------------------------------------------------------
    def handle_events(self):
        """Process OS and keyboard events; return False to quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r and self.game_over:
                    self.reset()    # restart on 'R' after game over
        return True

    def spawn_asteroids(self, dt: float):
        """Spawn new asteroids at the rate defined for the current level.

        Args:
            dt: elapsed time in seconds since last frame.
        """
        self.spawn_timer += dt
        interval = 1.0 / SPAWN_RATES[self.level_index]   # seconds between spawns
        while self.spawn_timer >= interval:
            self.asteroids.append(Asteroid(self.gravity_px))
            self.spawn_timer -= interval

    def update(self, dt: float):
        """Update all game objects, check collisions, and advance levels.

        Args:
            dt: elapsed time in seconds since last frame.
        """
        if self.game_over:
            return

        # Move the player ship
        self.ship.move(pygame.key.get_pressed())

        # Spawn, update, and cull asteroids
        self.spawn_asteroids(dt)
        for ast in self.asteroids:
            ast.update(dt)
        self.asteroids = [a for a in self.asteroids if not a.is_off_screen()]

        # Collision detection: axis-aligned bounding-box overlap
        for ast in self.asteroids:
            if self.ship.rect.colliderect(ast.rect):
                self.game_over = True
                return

        # Score increases with time survived (scaled by gravity for challenge)
        #self.score += dt * self.current_level["g"] * 3
        self.score += dt

        # Advance level when score threshold is reached and a next level exists
        if self.score >= TIME_PER_LEVEL * (self.level_index + 1):
            if self.level_index < len(LEVELS) - 1:
                self.level_index += 1
                self.asteroids.clear()
                self.spawn_timer = 0.0

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------
    def draw_hud(self):
        """Render the Heads-Up Display showing level, gravity, and score."""
        lvl  = self.current_level
        # Left side: level name and real gravity value
        label_level   = self.clock.render(
            f"Level {self.level_index + 1}: {lvl['name']}", True, (255, 255, 255))
        label_gravity = self.clock.render(
            f"Gravity: {lvl['g']:.2f} m/s²", True, lvl["color"])
        label_score   = self.clock.render(
            f"Score: {int(self.score)}", True, (220, 220, 100))

        self.screen.blit(label_level,   (10, 10))
        self.screen.blit(label_gravity, (10, 36))
        self.screen.blit(label_score,   (10, 62))

        # Thin coloured bar along the top to distinguish levels visually
        pygame.draw.rect(self.screen, lvl["color"], (0, 0, SCREEN_W, 4))

    def draw_game_over(self):
        """Display a centred Game Over message with the final score."""
        big_font  = pygame.font.SysFont(None, 64)
        small_font = pygame.font.SysFont(None, 32)
        msg1 = big_font.render("GAME OVER", True, (255, 60, 60))
        msg2 = small_font.render(f"Score: {int(self.score)}  |  Press R to restart",
                                 True, (200, 200, 200))
        self.screen.blit(msg1, msg1.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 - 40)))
        self.screen.blit(msg2, msg2.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 + 20)))

    def draw(self):
        """Render everything: background, asteroids, ship, HUD."""
        self.screen.fill(self.current_level["bg"])   # sky colour per body

        # Draw distant stars (static; seeded so they don't flicker each frame)
        rng = random.Random(42)
        for _ in range(80):
            sx = rng.randint(0, SCREEN_W)
            sy = rng.randint(0, SCREEN_H)
            pygame.draw.circle(self.screen, (255, 255, 255), (sx, sy), 1)

        for ast in self.asteroids:
            ast.draw(self.screen)

        self.ship.draw(self.screen)
        self.draw_hud()

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    # ------------------------------------------------------------------
    # Main entry-point
    # ------------------------------------------------------------------
    def run(self):
        """Start the game loop; runs until the player quits."""
        running = True
        while running:
            # dt capped at 0.05 s to prevent physics explosion after lag spikes
            dt = min(self.ticker.tick(FPS) / 1000.0, 0.05)
            running = self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    Game().run()

