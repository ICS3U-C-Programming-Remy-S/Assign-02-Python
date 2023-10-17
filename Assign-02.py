#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 16, 2023
# This program will ask the user for the units and
# the a side then display volume and surface area of
# a tetrahedron
import math


def main():
    # get the a side from the user
    print("This program will ask the user for the units and")
    print("the a side then display volume and surface area of")
    print("a tetrahedron.")
    a_side = float(input("Enter the a side of the tetrahedron: "))

    # get units from user
    units = input("Enter the units of the tetrahedron: ")

    # calculate the surface area and volume
    surface_area = math.sqrt(3) * (a_side**2)
    volume = (a_side**3) / (6 * math.sqrt(2))

    # error message for negative input
    if a_side < 0:
        print("")
        print("Please enter a valid value for the a side.")
    else:
        # display the surface area and volume
        print("")
        print("The surface area is = {:.2f} ".format(surface_area) + units + "^2")
        print("The volume is = {:.2f} ".format(volume) + units + "^3")


if __name__ == "__main__":
    main()
