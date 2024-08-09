import pygame as pg
pg.init()

width = 300
height = 600
gridsize = 30
grid_width = width // gridsize
grid_height = height // gridsize
white = (255, 255, 255)
black = (0, 0, 0)
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Tetris')
tetrominoes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]


def draw_grid():
    
    for x in range(0, width, gridsize):
        pg.draw.line(screen, white, (x, 0), (x, height))
    for y in range(0, height, gridsize):
        pg.draw.line(screen, white, (0, y), (width, y))



"""drawing shape"""



# Define the L object
class LObject:
    def __init__(self, x, y,s , mv=0):
        self.x = x
        self.y = y
        self.color = (255, 165, 255)
        self.shape = tetrominoes[s]

    def draw(self, surface):
        for y, row in enumerate(self.shape):
            for x, block in enumerate(row):
                if block == 1:
                    rect = pg.Rect((self.x + x) * gridsize, (self.y + y+mv) * gridsize, gridsize, gridsize)
                    pg.draw.rect(surface, self.color, rect)

# Create the L object and draw it on the screen



"""Drawing the shape ended"""
shp_type = 0
mv = 1


""""keep on moving down"""

timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, 1000)
xy_pos_shp = 4


"""keep on moving down ended"""
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN: # pressing key
# change shape
            if mv<1:
                if event.key == pg.K_UP:
                    shp_type += 1
                    if shp_type > 6:
                        shp_type = 0

                if event.key == pg.K_DOWN:
                    shp_type -= 1
                    if shp_type < 0:
                        shp_type = 6

# change position
                elif event.key == pg.K_LEFT:
                    xy_pos_shp -= 1
                    if xy_pos_shp < 0:
                        xy_pos_shp = 0


                elif event.key == pg.K_RIGHT:
                    xy_pos_shp += 1
            
        #this will update position
        if xy_pos_shp > 6 and shp_type == 0:
            xy_pos_shp = 6
        elif xy_pos_shp > 8 and shp_type == 1:
            xy_pos_shp = 8
        elif xy_pos_shp > 7 and shp_type >=2:
            xy_pos_shp = 7

        elif event.type == timer_event:
            if mv <18:
                mv += 1  # Move the object down
        

    # Add your game logic and drawing code here
    screen.fill(black)
    draw_grid()
    L_object = LObject(xy_pos_shp, 0, shp_type)
    
    L_object.draw(screen)
    pg.display.update()

pg.quit()