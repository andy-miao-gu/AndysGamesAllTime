import sys, pygame
pygame.init()
clicks=0
screen = pygame.display.set_mode( (600,400)  )
x = []
while(True):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicks=clicks+1
            print(clicks)
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.KEYDOWN:  
            # press space to print firing
            print("typing from keyboard")
            if event.key == pygame.K_SPACE:
                print("Firing")
        elif event.type == pygame.KEYUP:
            print("Lifted hands from keyboard")
            # when press space fire

        
    pygame.display.update()
