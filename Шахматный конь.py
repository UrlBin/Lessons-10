coordinates_of_horse = input("Ведите координату на доске, где стоит фигура коня: ")

row_coordinate = int(coordinates_of_horse[0])
column_coordinate = int(coordinates_of_horse[-1])

x = row_coordinate + 1
y = column_coordinate + 2
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate + 1
y = column_coordinate - 2
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate - 1
y = column_coordinate + 2
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate - 1
y = column_coordinate - 2
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates


x = row_coordinate + 2
y = column_coordinate + 1
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate + 2
y = column_coordinate - 1
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate - 2
y = column_coordinate + 1
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates

x = row_coordinate - 2
y = column_coordinate - 1
if x >= 0 and x <= 7 and y >= 0 and y <= 7:
    output_coordinates = tuple([x, y])
    print(output_coordinates)
    del output_coordinates