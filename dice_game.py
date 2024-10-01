from src import dice_class
import pygame

def main():
    dice_game = dice_class.Dice(2)

    pygame.init() 

    screen = pygame.display.set_mode([500,500])
    pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Dice Game')

    running = True
    while running: 
 
        for event in pygame.event.get(): 
        
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 
                    print("Left mouse")
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (0, 0, 255), (250,250), 75)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()

