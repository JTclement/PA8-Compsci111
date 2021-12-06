#Jacob Clement
#CompSci 111
#PA8
#Drop meteors

import random


def drop_meteors(met_list, met_dim, width):

    spawn_chance = randrange(0,100)
    x_pos = randrange(0, 780)

    if spawn_chance <= 5:

        met_pos = [x_pos, 0]
        met_list.append(met_pos)
                    

        


    
