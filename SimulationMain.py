import pygame as p
import Cards, Buttons
import random as r
import InfoPanel

DECK = []

def main():
    global deck, COUNT
    COUNT = 0 #used for total count
    setup() #creates window, basic pygame
    deck = createDeck() #assigns a secondary variable used in the info panel that is not changed - this way the values in the info panel will not be shuffled
    drawCardPanel() #draws the card panel
    initializeButtons() #initializes the buttons
    InfoPanel.init(screen, deck) #initializes info panel
    speed = 2 #sets a clock tick speed
    done = False #basic pygame
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                pass
                #done = True
            elif event.type == p.MOUSEBUTTONDOWN: #checks for a user click
                click = p.mouse.get_pos() #gets position of click
                if 0 <= click[0] < 175 and 400 <= click[1] <= 600: #checks coordinates of click compared to button location
                    speed += 1 #adds speed for speed up button
                elif 175 <= click[0] <= 350 and 400 <= click[1] <= 600: #lowers speed for speed down
                    if speed == 1: #these two lines prevent the speed from reaching 0 ("infinite" tick speed)
                        pass
                    else:
                        speed -= 1 #lowers speed if speed is greater than 1
        InfoPanel.reset(screen) #redraws specific parts of info panel to give impression of updating numbers
        InfoPanel.update(screen, deck, DECK) #updates the info panel's values
        reset() #resets the card panel
        updateCardPanelStats(COUNT, DECK) #updates the important stats shown on the card panel
        shuffleDeck() #shuffles the deck
        recentValue, recentSuit, COUNT = displayTopCard(COUNT) #displayTopCard draws the top card
        for i in range(52):
            if deck[i].suit == recentSuit and deck[i].value == recentValue:
                deck[i].count += 1 #this updates the second deck
        p.display.flip()
        clock.tick(speed)
    p.quit()


def initializeButtons(): #draws the buttons using a class and lists, along with their name in text and an image
    background = p.draw.rect(screen, 'black', (0, 400, 350, 200)) #creates a background for the template
    buttonNames = ['SPEED UP', 'SLOW DOWN'] #list of names
    colors = ['green', 'yellow'] #list of colors
    speedUpArrow = p.image.load("ArrowUp.png") #defines an arrow up for speed up
    speedDownArrow = p.image.load("ArrowUp.png") #arrow down for slow down
    speedDownArrow = p.transform.flip(speedDownArrow, False, True) #modify arrows
    speedUpArrow = p.transform.scale(speedUpArrow, (175, 200))
    speedDownArrow = p.transform.scale(speedDownArrow, (175, 200))
    arrowList = [speedUpArrow, speedDownArrow]
    buttons = [] #creates empty list for items to be appended to
    font = p.font.SysFont('Times New Roman', 25) #font
    template = p.Rect(0, 400, 175, 100) #template
    for i in range(2):
        button = Buttons.Button(buttonNames[i], colors[i]) #makes button variable
        buttons.append(button)
    for i in range(len(buttons)):
        buttonPos = template.clamp(background).move(i * 175, 75)
        p.draw.rect(screen, buttons[i].color, (0 + 175 * i, 400, 175, 200)) #draws the button
        screen.blit(arrowList[i], (175 * i, 400))
        line = font.render(buttons[i].name, True, 'purple')
        screen.blit(line, buttonPos.move(17 - i, 12)) #bolds the names
        screen.blit(line, buttonPos.move(18 - i, 12))
        screen.blit(line, buttonPos.move(19 - i, 12))
    return buttons


def drawCardPanel(): #draws the card panel - background and card
    background = p.image.load("PokerTable.jpg") #uses an image background
    background = p.transform.scale(background, (350, 400))
    shownCard = p.image.load("Card.png") #uses an image for the card
    shownCard = p.transform.scale(shownCard, (155, 250))
    screen.blit(background, (0, 0))
    screen.blit(shownCard, (100, 75))


def updateCardPanelStats(COUNT, DECK): #displays important statistics for the simulation
    font = p.font.SysFont('Times New Roman', 18)
    line = font.render('Total shuffles: ' + str(COUNT), True, 'black')
    screen.blit(line, (3, 0))
    cardFreqs = []
    for card in DECK:
        cardFreqs.append(card.count) #makes list of the count/frequency per card
    minCard = DECK[cardFreqs.index(min(cardFreqs))] #min card is the element at the index of the min value in cardfreqs, in the deck list
    minFreq = min(cardFreqs) #min freq is min for cardfreqs
    maxCard = DECK[cardFreqs.index(max(cardFreqs))] #max card is same as min card but max
    maxFreq = max(cardFreqs) #max freq is max for card freqs
    line = font.render('Most frequent top card: ' + str(maxCard.value) + str(maxCard.suit)
                       + ' with ' + str(maxFreq), True, 'black')
    screen.blit(line, (3, 25))
    line = font.render('Least frequent top card: ' + str(minCard.value) + str(minCard.suit)
                       + ' with ' + str(minFreq), True, 'black')
    screen.blit(line, (3, 50))



def reset(): #separate function to be more concise
    drawCardPanel()



def setup(): #sets up the code
    global screen, clock
    p.init()
    screen = p.display.set_mode((600, 600))
    clock = p.time.Clock()


def createDeck(): #creates the deck, a list of length 52 containing a combo of 13 values and 4 suits, simulating a standard playing deck
    suits = ['C', 'D', 'H', 'S']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = []
    for suit in suits:
        for value in values:
            DECK.append(Cards.Card(suit, value))
            deck.append(Cards.Card(suit, value))
    return deck

def displayTopCard(COUNT): #finds top card of deck then displays it, adding 1 to the count/frequency of that card
    font = p.font.SysFont('Times New Roman', 25)
    line = font.render(str(DECK[0].value) + DECK[0].suit, True, 'black')
    screen.blit(line, (160, 175))
    DECK[0].count += 1
    COUNT += 1
    return DECK[0].value, DECK[0].suit, COUNT


def shuffleDeck(): #shuffles the deck using the random library
    r.shuffle(DECK)



if __name__ == "__main__":
    main()