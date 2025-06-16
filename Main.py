import pygame
import sys
from pygame.locals import QUIT, Rect


Display_width = 800
Display_height = 800
Surface_width = 800
Surface_height = 800
display_ratio_x = Display_width / Surface_width
display_ratio_y = Display_height / Surface_height
FPS = 20
pygame.init()
DISPLAY = pygame.display.set_mode((Display_width, Display_height))
SURFACE = pygame.Surface((Surface_width, Surface_height))
FPSCLOCK = pygame.time.Clock()

pygame.display.set_caption("Minesweeper")
title_font = pygame.font.SysFont(None, 100, False, False)
title = title_font.render("Minesweeper", True, (31, 31, 31))

Difficulty = ("Easy", "Normal", "Hard", "Expert", "Insane")
Diff_color = ((0, 127, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (191, 0, 191))
Diff_color_edge = ((0, 63, 127), (0, 127, 0), (127, 127, 0), (127, 0, 0), (95, 0, 95))
Diff_font = pygame.font.SysFont(None, 35, False, False)

Diff_rect = []
Diff_img = []
for i in range(len(Difficulty)):
    rct = pygame.Rect(i*154 + 30, 150, 124, 80)
    img = pygame.Surface((124, 80))
    img.fill(Diff_color[i])
    pygame.draw.rect(img, Diff_color_edge[i], (0, 0, 124, 80), 3)
    txt = Diff_font.render(Difficulty[i], True, (31, 31, 31))
    img.blit(txt, (10, 10))
    Diff_rect.append(rct)
    Diff_img.append(img)


def main():
    channel = 0
    while True:
        pygame_events = pygame.event.get()
        for pygame_event in pygame_events:
            if pygame_event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((191, 191, 191))
        pygame.draw.rect(SURFACE, (0, 0, 0), (0, 0, 800, 800), 5)
        if channel == 0:
            SURFACE.blit(title, (50, 50))
            for k in range(len(Difficulty)):
                SURFACE.blit(Diff_img[k], Diff_rect[k].topleft)
        DISPLAY.blit(pygame.transform.scale(SURFACE, (Display_width, Display_height)), (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()