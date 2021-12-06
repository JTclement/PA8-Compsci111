#Jacob Clement
#CompSci 111
#PA8
#Draw meteors


def draw_meteors(met_list, met_dim, screen, yellow):

    for i in range(len(met_list)):

        pyg.draw.rect(screen, yellow, (met_list[i], met_dim))


    

    
