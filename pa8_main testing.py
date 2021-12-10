#Jacob Clement, Nick Gregarek, Trevor Cook, Andrew Arinas
#12/7/2021
#Programming Assignment #8
#Meteor game. Dodge meteors as they fall to the player to get a high score.
#The more meteors fall, the faster they get.



import pygame as pyg
import random
import matplotlib.pyplot as plt

def display_graph(graph_time_list, graph_score_list,score,time_counter):
    

    plt.plot(graph_time_list,graph_score_list, 'r-')
    plt.title('Score Report')
    plt.axis([0, time_counter, 0, score])
    plt.ylabel('Score')
    plt.xlabel('Time (seconds)')
    plt.show()
    




def set_speed(f_score):
    

    if f_score < 2:
        speed = 10
    else:
        speed = ((f_score // 2) * 2) + 10

    return speed

def draw_meteors(met_list, met_dim, screen, yellow):
    
    for i in range(len(met_list)):
        pyg.draw.rect(screen, yellow, (met_list[i][0], met_list[i][1], met_dim, met_dim))

        
        
def drop_meteors(met_list, met_dim, width):
    
    spawn_chance = random.randrange(0,100)
    x_pos = random.randrange(0, 780)
    
    if spawn_chance <= 7:
        met_pos = [x_pos, 0]
        met_list.append(met_pos)

        

def update_meteor_positions(met_list, height, score, speed):

    for i in range(len(met_list)-1):

        met_list[i][1] += speed

        if met_list[i][1] > height - 20:
            
            met_list.pop(i)
            score += 1
            
                
    return score


def detect_collision(meteor, player_pos, player_dim, met_dim):
    

    if meteor[1] >= 480 and meteor[1] <= 550:

        if meteor[0] <= player_pos[0] + 50 and meteor[0] >= player_pos[0]:

            return True


        elif meteor[0] + 20 <= player_pos[0] + 50 and meteor[0] + 20 >= player_pos[0]: 

                return True
        else:
            return False
    
    
    

def collision_check(met_list, player_pos, player_dim, met_dim):
    

    for meteor in met_list:

        collide = detect_collision(meteor, player_pos, player_dim, met_dim)

        if collide:

            return True
        else:
            return False


            

def main():
    
  
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code commented.
    '''

    pyg.init()                # initialize pygame

    time_counter = 0

    width = 800               # set width of game screen in pixels
    height = 600              # set height of game screen in pixels

    red = (255,0,0)           # rgb color of player
    yellow = (244,208,63)     # rgb color of meteors
    background = (0,0,156)    # rgb color of sky (midnight blue)

    player_dim = 50           # player size in pixels
    player_pos = [width/2, height-2*player_dim]  # initial location of player
                                                 # at bottom middle; height
                                                 # never changes

    met_dim = 20              # meteor size in pixels
    met_list = []             # initialize list of two-element lists
                              # giving x and y meteor positions

    background_image = pyg.image.load("space_background.png")



    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True, i.e., when collision
                              # is detected

    score = 0                 # initialize score
    graph_score_list = []
    graph_time_list = []

    clock = pyg.time.Clock()  # initialize clock to track time

    my_font = pyg.font.SysFont("monospace", 30) # initialize system font
    

    while not game_over:                       # play until game_over == True
        for event in pyg.event.get():          # loop through events in queue
            if event.type == pyg.KEYDOWN:      # checks for key press
                x = player_pos[0]              # assign current x position
                y = player_pos[1]              # assign current y position
                if event.key == pyg.K_LEFT:    # checks if left arrow;
                    x -= player_dim            # if true, moves player left
                elif event.key == pyg.K_RIGHT: # checks if right arrow;
                    x += player_dim            # else moves player right
                player_pos = [x, y]            # reset player position
            
        screen.blit(background_image, [0,0])
        #screen.fill(background_image)                # refresh screen bg color
        drop_meteors(met_list, met_dim, width) # read PA prompt
        speed = set_speed(score)               # read PA prompt
        score = update_meteor_positions(met_list, height, score, speed)
                                               # read PA prompt
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just think of
                                                   # blit to mean draw
        draw_meteors(met_list, met_dim, screen, yellow) # self-explanatory;
                                                        # read PA prompt

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))                                        # draw player

        if collision_check(met_list, player_pos, player_dim, met_dim):
            game_over = True                       # read PA prompt
    
        clock.tick(30)                             # set frame rate to control
                                                   # frames per second (~30); 
                                                   # slows down game
        time_counter += (1/30)

        

        graph_score_list.append(score)
        graph_time_list.append(time_counter)
            
            


        pyg.display.update()                       # update screen characters






    # Outside while-loop now.
    print('Final score:', score)                   # final score
    score_text = my_font.render('Final Score:' + str(score), True, yellow, red)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (width // 2, height // 2 + 50)

    info_text = my_font.render('Click The Right Arrow to View Your Stats', True, yellow, red)
    info_text_rect = info_text.get_rect()
    info_text_rect.center = (width // 2, height // 2 + 100)

    endgame_text = my_font.render('Game Over', True, yellow, red)
    text_rect = endgame_text.get_rect()
    text_rect.center = (width // 2, height // 2)
    
    screen.blit(endgame_text, text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(info_text, info_text_rect)

   

    

    
    pyg.display.update()
    close = False
    while not close:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    close = True
            elif event.type == pyg.KEYDOWN:

                if event.key == pyg.K_RIGHT:
                    close = True
                    display_graph(graph_time_list,graph_score_list, score, time_counter)
                    
                
    

    pyg.quit() # leave pygame
    #display_graph(graph_time_list,graph_score_list, score, time_counter)
    

main()
