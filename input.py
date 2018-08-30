import pygame, random, time, os
pygame.init()
white = (255,255,255)
silver = (211,211,211)
pygame.display.init()
GameBoard = pygame.display.set_mode((700, 600))
clock = pygame.time.Clock()
def input():
    TEXT = []
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(10, 560, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        TEXT.append(text)
                        print(TEXT)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pygame.draw.rect(GameBoard, silver, [10, 560, 200, 32])
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        GameBoard.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(GameBoard, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
