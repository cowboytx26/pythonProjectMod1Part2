# Author:  Brian Wiatrek
# Date written: 06/08/24
# Assignment:   Module 1 exercise 2 part 2
# Short Desc:   This is a python program that will calculate the surface area of a cube
# intCubeEdge: this variable contains the length of the edge of the cube
# intCubeSurfaceArea: this variable contains the surface area of the cube
# strHeader: this variable contains the text printed as a label to the user

def cubeSurfaceArea(intLength):
    """
    This function takes as user input the length of the edge of a cube and calculates the surface area
    The formula of the surface area of a cube is length squared times six
    """
    return 6*intLength**2


print(cubeSurfaceArea.__doc__)
strHeader = 'The surface area of the cube is: '
try:
    intCubeEdge = int(input("Please enter the length of the edge of the cube\n"))
except ValueError:
    print("Please enter an integer value")
    exit(1)
intCubeSurfaceArea = cubeSurfaceArea(intCubeEdge)
print(strHeader, intCubeSurfaceArea)
