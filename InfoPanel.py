import pygame as p

def init(screen, deck): #initiates the info panel
    global panel, font
    panel = p.draw.rect(screen, 'black', (350, 0, 250, 600))
    font = p.font.SysFont('Times New Roman', 14)
    for i in range(13):
        for j in range(4):
            line = font.render(str(deck[i + j * 13].value) + deck[i + j * 13].suit, True, 'green2') #displays the value-suit combo of each card
            screen.blit(line, panel.move(((250 / 8) * 2 * j), ((600 // 13) * i)))


def update(screen, deck, DECK):
    for i in range(13):
        for j in range(4):
            line = font.render(str(deck[i + j * 13].value) + deck[i + j * 13].suit, True, 'green2') #redraws the value-suit combo
            screen.blit(line, panel.move(((250 / 8) * 2 * j), ((600 // 13) * i)))
            line = font.render(str(deck[i + j * 13].count), True, 'green2') #displays the count for each corresponding card
            screen.blit(line, panel.move(((250 / 8) * 2 * j + 25), ((600 // 13) * i)))


def reset(screen):
    #for j in range(4):
    resetRect = p.draw.rect(screen, 'black', (350, 0, 250, 600)) #redraws the entire background for the info panel