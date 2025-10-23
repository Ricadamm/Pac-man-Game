import pygame
from gamesettings import WIDTH, HEIGHT, NAV_HEIGHT


class Display:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("arial", 24, bold=True)
        self.white = pygame.Color("white")

    def show_life(self, life_count):
        for i in range(life_count):
            pygame.draw.circle(
                self.screen,
                pygame.Color("red"),
                (30 + i * 40, HEIGHT + NAV_HEIGHT // 2),
                12,
            )

    def show_level(self, level):
        text = self.font.render(f"LEVEL: {level}", True, self.white)
        self.screen.blit(text, (WIDTH // 2 - 60, HEIGHT + 15))

    def show_score(self, score):
        text = self.font.render(f"SCORE: {score}", True, self.white)
        self.screen.blit(text, (WIDTH - 180, HEIGHT + 15))

    def game_over(self):
        over_font = pygame.font.SysFont("arial", 48, bold=True)
        text = over_font.render("GAME OVER - Press R to Restart", True, pygame.Color("red"))
        self.screen.blit(text, (WIDTH // 2 - 300, HEIGHT // 2))
