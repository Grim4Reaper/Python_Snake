import pygame, time, sys, random
from pygame.locals import *

hardness = 20
pygame.init()
screen = pygame.display.set_mode((800,800))
p1_snake = [[0,0],[0,0],[0,0]]
p1_direction = 'RIGHT'
p2_snake = [[0,790],[0,790],[0,790]]
p2_direction = 'LEFT'
food_list = []
food_types = ['normal', 'normal', 'normal', 'normal']
p1_add_length = 5
p2_add_length = 5
clock = pygame.time.Clock()
speed = 90
p1_die = False
p2_die = False
p1_score = 0
p2_score = 0

def Food():
    food = {
    'pos': (random.randint(0, 79) * 10, random.randint(0, 79) * 10),
    'type': random.choice(food_types),
    'time': 0
    }
    return food

def Add_Food():
    global food_list
    food_list.append(Food())
    
def Eat():
    global food, p1_die, p2_die, p1_add_length, p2_add_length, p2_score, p1_score
    for f in food_list:  
        if (f['pos'][0] - 10) < p1_snake[0][0] < (f['pos'][0] + 10):
            if (f['pos'][1] - 10) < p1_snake[0][1] < (f['pos'][1] + 10):
                if f['type'] == 'normal':
                    p1_add_length += 1
                    p1_score += 1
                else:
                    p1_snake.pop()
                    food_list.remove(f)
        if (f['pos'][0] - 10) < p2_snake[0][0] < (f['pos'][0] + 10):
            if (f['pos'][1] - 10) < p2_snake[0][1] < (f['pos'][1] + 10):
                if f['type'] == 'normal':
                    p2_add_length += 1
                    p2_score += 1
                else:
                    p2_snake.pop()
                    food_list.remove(f)
                    if not p2_snake:
                        p2_die = True
        
def Food_On_Snake():
    global food
    for x in range(len(p1_snake) - 1):
        for f in food_list:
                if (f['pos'][0] - 10) < p1_snake[x + 1][0] and (f['pos'][0] + 10) > p1_snake[x + 1][0]: 
                    if (f['pos'][1] - 10) < p1_snake[x + 1][1] and (f['pos'][1] + 10) > p1_snake[x + 1][1]: 
                        food_list.remove(f)    
    for x in range(len(p2_snake) - 1):
        for f in food_list:
                if (f['pos'][0] - 10) < p2_snake[x + 1][0] and (f['pos'][0] + 10) > p2_snake[x + 1][0]: 
                    if (f['pos'][1] - 10) < p2_snake[x + 1][1] and (f['pos'][1] + 10) > p2_snake[x + 1][1]: 
                        food_list.remove(f)           
                        
def Show():
    for section in p1_snake:
        pygame.draw.rect(screen, (0,0,255), ((section[0], section[1]), (10, 10)))
    for section in p2_snake:
        pygame.draw.rect(screen, (0,255,0), ((section[0], section[1]), (10, 10)))    
    while len(food_list) < hardness:
            Add_Food()            
    for food in food_list:
        food['time'] += 1
        if food['type'] == 'normal':
            pygame.draw.rect(screen, (200,0,0), ((food['pos'][0], food['pos'][1]), (10, 10)))
        elif food['type'] == 'poisonous':
            if food['time'] > 100:
                food_list.remove(food)
            else:
                pygame.draw.rect(screen, (255,0,0), ((food['pos'][0], food['pos'][1]), (10, 10)))       
        else:
            pygame.draw.rect(screen, (255,215,0), ((food['pos'][0], food['pos'][1]), (10, 10)))
        Font = pygame.font.Font('simhei.ttf', 20)
        text = f'player1 score: {p1_score}  player2 score: {p2_score}'
        Text = Font.render(text,True,(0,0,0))
        screen.blit(Text, (800 - 10 * len(text), 10))
                
def Move_Snake():
    global p1_snake, p2_snake, p1_add_length, p2_add_length
    if p1_direction == 'UP':
        p1_snake.insert(0, [p1_snake[0][0], p1_snake[0][1] - 10])
    elif p1_direction == 'RIGHT':
        p1_snake.insert(0, [p1_snake[0][0] + 10, p1_snake[0][1]])
    elif p1_direction == 'DOWN':
        p1_snake.insert(0, [p1_snake[0][0], p1_snake[0][1] + 10])
    elif p1_direction == 'LEFT':
        p1_snake.insert(0, [p1_snake[0][0] - 10, p1_snake[0][1]])
    if p1_add_length == 0: 
        p1_snake.pop()
    if p1_add_length > 0:
        p1_add_length -= 1
    if p2_direction == 'UP':
        p2_snake.insert(0, [p2_snake[0][0], p2_snake[0][1] - 10])
    elif p2_direction == 'RIGHT':
        p2_snake.insert(0, [p2_snake[0][0] + 10, p2_snake[0][1]])
    elif p2_direction == 'DOWN':
        p2_snake.insert(0, [p2_snake[0][0], p2_snake[0][1] + 10])
    elif p2_direction == 'LEFT':
        p2_snake.insert(0, [p2_snake[0][0] - 10, p2_snake[0][1]])
    if p2_add_length == 0: 
        p2_snake.pop()
    if p2_add_length > 0:
        p2_add_length -= 1
    
def Turn():
    global p1_direction, p2_direction
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            raise SystemExit  
        if event.type == KEYDOWN:
            if event.key == K_LEFT and p1_direction != 'RIGHT':
                p1_direction = 'LEFT'
            elif event.key == K_RIGHT and p1_direction != 'LEFT':
                p1_direction = 'RIGHT'
            elif event.key == K_UP and p1_direction != 'DOWN':
                p1_direction = 'UP'
            elif event.key == K_DOWN and p1_direction != 'UP':
                p1_direction = 'DOWN'
            if event.key == K_a and  p2_direction != 'RIGHT':
                p2_direction = 'LEFT'
            elif event.key == K_d and  p2_direction != 'LEFT':
                p2_direction = 'RIGHT'
            elif event.key == K_w and p2_direction != 'DOWN':
                p2_direction = 'UP'
            elif event.key == K_s and p2_direction != 'UP':
                p2_direction = 'DOWN'        
                
def Hit_Edge():
    global p1_snake, p2_snake
    if p1_snake[0][0] > 800:
        p1_snake[0][0] = 0
    elif p1_snake[0][0] < 0:
        p1_snake[0][0] = 800
    if p1_snake[0][1] > 800:
        p1_snake[0][1] = 0
    elif p1_snake[0][1] < 0:
        p1_snake[0][1] = 800
    if p2_snake[0][0] > 800:
        p2_snake[0][0] = 0
    elif p2_snake[0][0] < 0:
        p2_snake[0][0] = 800
    if p2_snake[0][1] > 800:
        p2_snake[0][1] = 0
    elif p2_snake[0][1] < 0:
        p2_snake[0][1] = 800    
        
def Die():
    global p1_die, p2_die, p1_snake, p2_snake, food_list
    if len(p1_snake) <= 1:
            p1_die = True
    if len(p2_snake) <= 1:
            p2_die = True 
    if p1_die:
        p1_snake = [[20,0],[10,0],[0,0]]
        p1_direction = 'RIGHT'
        p1_die = False
    if p2_die:
        p2_snake = [[20,0],[10,0],[0,0]]
        p2_direction = 'LEFT'
        p2_die = False
        
def Collision():
    global p1_die, p2_die, p1_score, p2_score, p1_snake, p2_snake, p1_add_length, p2_add_length
    if p1_snake[0] ==  p2_snake[0]:
        if len(p1_snake) > len(p2_snake):
            p2_die = True
            p1_score += len(p2_snake)
            p1_add_length += len(p2_snake)
        elif len(p2_snake) > len(p1_snake):
            p1_die = True
            p2_score += len(p1_snake)
            p2_add_length += len(p1_snake)
        else:
            p2_die = True
            p1_die = True
        return 0
    
    for body in p2_snake:
        if p1_snake[0] == body:
            p1_die = True
            p2_score += len(p1_snake)
            p2_add_length += len(p1_snake)
    for body in p1_snake:
        if p2_snake[0] == body:
            p2_die = True
            p1_score += len(p2_snake)
            p1_add_length += len(p2_snake)

def main():
    while True:
        screen.fill((255, 255, 255))
        Collision()
        Die()
        Food_On_Snake()
        Show()
        Food_On_Snake()
        Eat()
        Move_Snake()
        Turn()
        Hit_Edge()
        pygame.display.update()
        clock.tick(speed)
    
def Loading_Screen():
    Play = False   
    font = pygame.font.Font('simhei.ttf', 50)
    Background = pygame.image.load('bac2.png')
    Background = pygame.transform.smoothscale(Background, (800,800))
    Text = ['Snake', 'Press 1 for help', 'Click to start']    
    while Play == False:
        screen.blit(Background, (0, 0))
        for x in range(len(Text)):
            text = font.render(Text[x],True,(255,0,0))
            screen.blit(text, (100, 90 + 60 * x))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                Play = True       
            if event.type == KEYDOWN:
                if event.key == K_1:
                    Text2 = ['red food - Poison', 'dark red food - Normal', 'Try to kill the other player ', 'get as long as possible', 'normal slither.io rules apply', 'Player 1 use arrow keys', 'Player 2 use WASD', 'player1: blue   player 2: green', '', 'Click to exit']
                    view = True
                    while view:
                        screen.fill((255, 255, 255))
                        for x in range(len(Text2)):
                            text = font.render(Text2[x],True,(255,0,0))
                            screen.blit(text, (10, 10 + 60 * x))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                raise SystemExit
                            if event.type == MOUSEBUTTONDOWN:
                                view = False                                 

Loading_Screen()
main()
