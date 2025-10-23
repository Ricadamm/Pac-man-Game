import pygame
import heapq
from gamesettings import CHAR_SIZE, GHOST_SPEED


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index, color):
        super().__init__()
        self.image = pygame.Surface((CHAR_SIZE, CHAR_SIZE))
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_index * CHAR_SIZE, y_index * CHAR_SIZE)

        self.start_pos = self.rect.topleft
        self.move_speed = GHOST_SPEED
        self.color = color

    def update(self, walls, target_rect):
        start = (self.rect.centerx // CHAR_SIZE, self.rect.centery // CHAR_SIZE)
        goal = (target_rect.centerx // CHAR_SIZE, target_rect.centery // CHAR_SIZE)

        path = self._a_star(start, goal, walls)
        if len(path) > 1:
            next_cell = path[1]  
            dx = next_cell[0] * CHAR_SIZE - self.rect.centerx
            dy = next_cell[1] * CHAR_SIZE - self.rect.centery

            if abs(dx) > abs(dy):
                self.rect.x += self.move_speed if dx > 0 else -self.move_speed
            elif abs(dy) > 0:
                self.rect.y += self.move_speed if dy > 0 else -self.move_speed

    def _a_star(self, start, goal, walls):
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        wall_set = { (w.x // CHAR_SIZE, w.y // CHAR_SIZE) for w in walls }
        open_set = [(0, start)]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: heuristic(start, goal)}

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                return self._reconstruct_path(came_from, current)

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if neighbor in wall_set or neighbor[0] < 0 or neighbor[1] < 0:
                    continue
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    if neighbor not in [n for _, n in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return [start]

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path

    def move_to_start_pos(self):
        self.rect.topleft = self.start_pos
