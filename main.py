import pygame
import sys
import random
pygame.init()

WINDOW = pygame.display.set_mode((1024,720))

pygame.display.set_caption("DragonBall")

#font game
font_title = pygame.font.Font("font_game.ttf",32)
text_title = font_title.render("Dragon Ball",True,"Red","Pink")
width_title = text_title.get_rect()

#load dragon
x_goku,y_goku = 50,50

image_goku = pygame.transform.scale(pygame.image.load("goku.png","goku"),(50,50))
goku = pygame.Rect(x_goku,y_goku,image_goku.get_width(),image_goku.get_height())
# dragon = pygame.Rect()

#load gem
x_gem,y_gem = random.randint(10,1024), random.randint(10,720)
image_gem = pygame.transform.scale(pygame.image.load("gem.png"),(50,50))
gem = pygame.Rect(x_gem,y_gem,image_gem.get_width(),image_gem.get_height())


#đơn vị di chuyển
distance = 100

#setup time 
random_interval = 10000 #10 giây
#thời gian bắt đầu lặp
last_time = pygame.time.get_ticks()

#điểm
score = 0
score_font = pygame.font.Font(None,32)
score_text = score_font.render(f"""Score: {score}""",True,"Red","Pink")
score_x,score_y = 1000 - score_text.get_width(), 10



# Background
while True:
    WINDOW.fill("White")
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         #điều hướng goku
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_goku -= distance
            if event.key == pygame.K_DOWN:
                y_goku += distance
            if event.key == pygame.K_LEFT:
                x_goku -= distance
            if event.key == pygame.K_RIGHT:
                x_goku += distance
            x = (1024-width_title.width)//2
          

            if goku.colliderect(gem):
                    score += 10
                    score_text = score_font.render(f'''Score: {score}''',True,"Red","Pink")
                    #tăng điểm sau đó random vị trí
                    x_gem,y_gem = random.randint(10,1024), random.randint(10,720)
  
    current_time = pygame.time.get_ticks()

    font = pygame.font.Font(None,30)
    text = font.render(str(current_time),True,"Red")

    WINDOW.blit(text_title,((1024 - text_title.get_width())//2,10))
    WINDOW.blit(score_text,(score_x,score_y))
    if ((current_time - last_time) % random_interval == 0): 
        x_gem,y_gem = random.randint(10,1024), random.randint(10,720)

    goku = pygame.Rect(x_goku,y_goku,image_goku.get_width(),image_goku.get_height())
    gem = pygame.Rect(x_gem,y_gem,image_gem.get_width(),image_gem.get_height())
    if (current_time // 500 % 2) == 0: 
        WINDOW.blit(image_gem,(x_gem,y_gem))
    
    WINDOW.blit(image_goku,(x_goku,y_goku))


 

    # WINDOW.blit(text,(500,500))

    pygame.display.update()

        