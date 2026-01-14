import pygame
import random

pygame.init()
WIDTH, HEIGHT = 1000, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amogus FFA: All Variants")

FONT = pygame.font.SysFont("arial", 14)

# Colors (cycled for visibility)
COLORS = [
    (255, 0, 0), (0, 128, 255), (255, 255, 0), (0, 255, 128),
    (255, 0, 255), (255, 128, 0), (128, 0, 255), (0, 255, 255),
    (100, 255, 100), (200, 100, 255), (255, 200, 100), (128, 255, 0),
    (100, 100, 100), (0, 100, 200), (255, 100, 100), (50, 200, 150),
]

# All Amogus variants
NAMES = [
    "Amogus", "Asmolgus", "Abigus", "Amoooogus", "Og Amogus", "Agodus", "Amoamomomogusgus",
    "Beefor", "Mogus", "Amoamogus", "AAAAAA", "Amomogus", "Amoma", "Sugus",
    "Amomoma", "Oh Yeah", "What If", "A", "USA", "As", "Agusmo", "Gypsus"
]

class Impostor:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.rect = pygame.Rect(x, y, 28, 28)
        self.speed = 2
        self.alive = True

    def move(self):
        dx, dy = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
            name_text = FONT.render(self.name, True, (255, 255, 255))
            surface.blit(name_text, (self.rect.x, self.rect.y - 15))

    def attack(self, others):
        for other in others:
            if other == self or not other.alive:
                continue
            if self.rect.colliderect(other.rect):
                if other.name == "Agodus" and self.name != "Mogus":
                    print(f"{self.name} tried to attack Agodus. SMITED.")
                    self.alive = False
                    smite_effect(win, self.rect.center)
                    return
                print(f"{self.name} eliminated {other.name}!")
                other.alive = False

def smite_effect(surface, pos):
    for _ in range(2):
        pygame.draw.line(surface, (255, 255, 0), (pos[0] - 20, pos[1] - 40), pos, 3)
        pygame.draw.line(surface, (255, 255, 0), (pos[0] + 20, pos[1] - 40), pos, 3)
        pygame.display.update()
        pygame.time.wait(80)

# Spawn impostors with color cycling
impostors = [Impostor(name, COLORS[i % len(COLORS)], random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)) for i, name in enumerate(NAMES)]

clock = pygame.time.Clock()
running = True

while running:
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for imp in impostors:
        if imp.alive:
            imp.move()
            imp.attack(impostors)
        imp.draw(win)

    pygame.display.update()
    clock.tick(48000)

pygame.quit()