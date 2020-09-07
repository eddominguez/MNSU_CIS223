#problem 5: time calculator
#Edward Dominguez
def main():
    
    
    speed_of_light = 186000
    
    #user inputs how many miles the photo will travel
    distance = int(input("How many miles is the photo traveling? :"))
    
    #user input used for the calculation
    time_taken = (distance / speed_of_light)
    
    print("The time it would take is: " , time_taken, "seconds")
    
main()