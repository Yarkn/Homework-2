import math

# This function takes a parameter num which is the total number of tuples that will be input by the user.
# Then, it creates a list of coordinates in the form [(x,y)]
def create_list(num):
    while num > 0:
        print("Please specify the coordinate tuple in (x, y) format.")
        input_coordinates = input()
        
        coordinates = (int(input_coordinates.split(',')[0][1:]) , int(input_coordinates.split(',')[1].split(')')[0]))
        
        coordinate_list.append(coordinates)
        num -= 1
        
    print("Coordinate list is the following: ")
    print(coordinate_list)
    print()

# This function calculates the center of mass of all coordinates given by the user.
# Then, it returns a tuple containing the x and y coordinates of the center of mass
#  in the form: (x,y)
def calculate_com(num):
    x     = 0
    y     = 0
    index = 0
    while num > 0:
        x     += coordinate_list[index][0]
        y     += coordinate_list[index][1]
        num   -= 1
        index += 1
        
    x = x / index
    y = y / index
    
    print("Center of mass is: ", (x,y))
    return (x, y)
    
# This function calculates the euclidean distance between all coordinates given by the
#  user and the center of mass.
# Then, it stores these distance values in the euclidean_list variable.
def euclidean_distance(num):
    x     = 0
    y     = 0
    index = 0
    while num > 0:
        x     += (com[0] - coordinate_list[index][0])**2
        y     += (com[1] - coordinate_list[index][1])**2
        
        euclidean = math.sqrt(x + y)
        euclidean_list.append(euclidean)
        num      -= 1
        index    += 1
    
    print("The list of euclidean distances is: ", euclidean_list)


# This function finds the minimum and maximum elements in the euclidean list
#  which are the closest and farthest coordinates.
def closest_and_farthest(num):
    index = 0
    minimum = min(euclidean_list)
    maximum = max(euclidean_list)
    while num > 0:
        if minimum == euclidean_list[index]:
            print("Closest point is : ", coordinate_list[index])
        if maximum == euclidean_list[index]:
            print("Farthest point is: ", coordinate_list[index])
        index += 1
        num   -= 1
    


if __name__ == "__main__":
    
    coordinate_list = []

    print("Please enter how many coordinates will be given.")
    s = input()
    
    # read total number of coordinates
    numofelements = int(s)
    print("Number of coordinate tuples is: ", numofelements)
    
    # create_list function call
    create_list(numofelements)
    # calculate_com function call
    com = calculate_com(numofelements)
    
    euclidean_list = []
    
    # euclidean_distance function call
    # calculate all euclidean distances, and save them to euclidean_list
    euclidean_distance(numofelements)
    
    # closest_and_farthest function call
    closest_and_farthest(numofelements)