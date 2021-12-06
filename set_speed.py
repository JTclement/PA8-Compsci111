#Jacob Clement
#CompSci 111
#PA8
#Set speed function







def set_speed(score):

    
    if score < 2:

        speed = 100
    else:
        speed = ((score // 2) * 50) + 10
    
    
        
    

    return speed




def main():

    score = 0
    
    
    

    for i in range(10):

        score += 1
        speed = set_speed(score)
        
        
        
    print(speed)
    print(score)

        


main()
