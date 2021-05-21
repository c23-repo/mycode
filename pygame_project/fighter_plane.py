#!/usr/bin/python3
import os
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # os.path.join("game_assets/images/", "plane.png") goes inside the load function
        self.surf = pygame.image.load(os.path.join("game_assets/images", "plane.png")).convert()
        self.surf = pygame.transform.scale(self.surf, (85, 35))
        self.surf.convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user key presses
    def update(self, key_press):
        if key_press[K_UP]:
            self.rect.move_ip(0, -10)
        if key_press[K_DOWN]:
            self.rect.move_ip(0, 10)
        if key_press[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if key_press[K_RIGHT]:
            self.rect.move_ip(10, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def exploded(self):
        self.surf = pygame.image.load(os.path.join("game_assets/images", "explosion.png")).convert()


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super(Missile, self).__init__()
        self.surf = pygame.image.load(os.path.join("game_assets/images", "missile.png")).convert()
        self.surf = pygame.transform.scale(self.surf, (65, 28))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join("game_assets/images", "cloud.png")).convert()
        self.surf = pygame.transform.scale(self.surf, (75, 75))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# Initialize pygame
pygame.init()
pygame.mixer.init()


AUDIO = pygame.mixer.music
FONT = pygame.font.SysFont("Helvetica", 20, True)
TEXT_COLOR = (255, 255, 255)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load(os.path.join("game_assets/images", "BG.png")).convert()

# Setup the clock for frame rates
clock = pygame.time.Clock()
# Setup timer for clock count, speed increase, and score
start_time = None

# Create a custom event for adding a new enemy
ADD_MISSILE = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_MISSILE, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

player_plane = Player()

# Create groups to hold enemy sprites and all sprites
# - missiles is used for collision detection and position updates
# - all_sprites is used for rendering
missiles = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player_plane)


def up_difficulty(seconds):
    increase = 0
    if round(seconds, 0) % 10 == 0:
        increase = seconds / 10
    return increase


# Variable to keep the main loop running
running = True
frames = 30
time_counter = 0
frame_increase = 0

AUDIO.load(os.path.join("game_assets/audio", "Nighttime-Escape.mp3"))
AUDIO.set_volume(0.30)
AUDIO.play(-1)

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            # Initiate start time
            if start_time is None:
                start_time = pygame.time.get_ticks()

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy
        elif event.type == ADD_MISSILE:
            # Create the new missile and add it to sprite groups
            new_missile = Missile()
            missiles.add(new_missile)
            all_sprites.add(new_missile)

        # Add a new cloud
        elif event.type == ADD_CLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player_plane.update(pressed_keys)

    # Update enemy position
    missiles.update()
    clouds.update()

    # Fill the screen with black
    screen.blit(background_image, [0, 0])

    # Draw the player on the screen
    screen.blit(player_plane.surf, player_plane.rect)

    if start_time:
        time_since_enter = int((pygame.time.get_ticks() - start_time) / 1000)
        time_counter += time_since_enter
        message = 'Time: ' + str(time_since_enter)
        screen.blit(FONT.render(message, True, TEXT_COLOR, (0, 0, 0)), (680, 840))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player_plane, missiles):
        # If so, then remove the player and stop the loop
        player_plane.kill()
        player_plane.exploded()
        running = False

    # Update the display
    pygame.display.flip()

    # Lines 220-21 are supposed to increase the speed of the game
    # frame_increase = up_difficulty(time_counter)
    # frames += frame_increase
    print("THIS IS THE FPS INCREASE", frame_increase)
    print("This is the new frames per second", frames)
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(frames)

pygame.quit()
