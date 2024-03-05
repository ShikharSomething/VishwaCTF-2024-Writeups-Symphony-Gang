
from PIL import Image, ImageDraw


def read_coordinates_from_file():
    coordinates = []

    with open("5ecr3t_c0de.txt", 'r') as file:
        for line in file:
            cleaned_line = line.replace('(', '').replace(')', '')
            x, y = map(int, cleaned_line.strip().split(','))  
            coordinates.append((x, y))

    return coordinates

coordinates = []
coordinates = read_coordinates_from_file()


width, height = 4000, 2000  
image = Image.new("RGB", (width, height), "white")


draw = ImageDraw.Draw(image)
point_radius = 2  

for x, y in coordinates:
    draw.ellipse((x - point_radius, y - point_radius, x + point_radius, y + point_radius), fill="red")


image.save("output_image.png")
