import pygame
from gamesettings import CHAR_SIZE, PLAYER_SPEED


class Pac(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        super().__init__()

        self.image = pygame.Surface((CHAR_SIZE, CHAR_SIZE))
        self.image.fill(pygame.Color("yellow"))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_index * CHAR_SIZE, y_index * CHAR_SIZE)

        self.speed = PLAYER_SPEED
        self.direction = pygame.Vector2(0, 0)
        self.status = "idle"
        self.pac_score = 0
        self.life = 3
        self.immune = False
        self.immune_time = 0
        self.start_pos = self.rect.topleft

    def animate(self, pressed_keys, walls):
        dx, dy = 0, 0
        if pressed_keys[pygame.K_UP]:
            dy = -self.speed
        elif pressed_keys[pygame.K_DOWN]:
            dy = self.speed
        elif pressed_keys[pygame.K_LEFT]:
            dx = -self.speed
        elif pressed_keys[pygame.K_RIGHT]:
            dx = self.speed

        if dx != 0 or dy != 0:
            self.direction = pygame.Vector2(dx, dy)
            self.status = "moving"
        else:
            self.status = "idle"

        future_rect = self.rect.move(dx, dy)
        if not any(future_rect.colliderect(w) for w in walls):
            self.rect = future_rect

        if self.immune_time > 0:
            self.immune_time -= 1
            self.immune = True
            if self.immune_time % 10 < 5:
                self.image.fill(pygame.Color("gold"))
            else:
                self.image.fill(pygame.Color("yellow"))
        else:
            self.immune = False
            self.image.fill(pygame.Color("yellow"))

    def move_to_start_pos(self):
        self.rect.topleft = self.start_pos
        self.direction = pygame.Vector2(0, 0)
        self.status = "idle"

    def update(self):
        pass
