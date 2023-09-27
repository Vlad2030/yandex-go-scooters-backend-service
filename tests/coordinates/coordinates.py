import time
import random


def generate_objects(
        start_pos_x: int,
        start_pos_y: int,
        count: int,
) -> list[list[float]]:
    objects = []

    for obj in range(count):
        pos_x = start_pos_x + random.randint(0, 999999) / 1000000
        pos_y = start_pos_y + random.randint(0, 999999) / 1000000
        objects.append([pos_x, pos_y])

    return objects


def calculate_shape_points(
        pos1: list[float],
        pos2: list[float],
) -> list[list[float]]:
    pos1_x, pos1_y = pos1
    pos2_x, pos2_y = pos2

    pos3_x = pos1_x
    pos3_y = pos2_y

    pos4_x = pos2_x
    pos4_y = pos1_y

    pos3 = [pos3_x, pos3_y]
    pos4 = [pos4_x, pos4_y]

    shape_points = [pos1, pos2, pos3, pos4]
    return shape_points


def search_objects(
        objects: list[float],
        shape: list[list[float]],
) -> list[list[float]]:
    founded_objects = []

    pos1, pos2, pos3, pos4 = shape
    pos1_x, pos1_y = pos1
    pos2_x, pos2_y = pos2

    for obj in objects:
        pos_x, pos_y = obj

        if (pos_x >= pos2_x and pos_x <= pos1_x
                and pos_y >= pos1_y and pos_y <= pos2_y):
            founded_objects.append(obj)

    return founded_objects

python_start = time.perf_counter()

pos1 = [55.767351, 37.558771]
pos2 = [55.761848, 37.570799]

objects_start = time.perf_counter()
objects = generate_objects(
    start_pos_x=55.000000,
    start_pos_y=37.000000,
    count=50_000,
)
objects_end = time.perf_counter() - objects_start

shape_start = time.perf_counter()
pos_points = calculate_shape_points(pos1, pos2)
shape_end = time.perf_counter() - shape_start

search_start = time.perf_counter()
founded_objects = search_objects(objects, pos_points)
search_end = time.perf_counter() - search_start


print(f"GENERATION TIME")
print(f"objects time:\t{objects_end:.5f} secs")
print(f"shape time:\t{shape_end:.5f} secs")
print(f"search time:\t{search_end:.5f} secs")
print()
print("SEARCH POS")
print(f"pos1:\t{pos1}")
print(f"pos2:\t{pos2}")
print()
print("SHAPE")
[print(f"pos{number}:\t{point}") for number, point in enumerate(pos_points, 1)]
print()
print(f"OBJECTS: {len(objects)}")
if len(objects) <= 20:
    [print(f"{number}.\tobj:\t{obj}") for number, obj in enumerate(objects, 1)]
print()
print(f"FOUNDED OBJECTS ({len(founded_objects)})")
if len(founded_objects) <= 20:
    [print(f"{number}.\tobj:\t{obj}") for number, obj in enumerate(founded_objects, 1)]

python_end = time.perf_counter() - python_start
from coordinates import main

cython_start = time.perf_counter()
founded_objects = main()
cython_end = time.perf_counter() - search_start

print()
print("EXECUTION TIME")
print(f"python time:\t{python_end:.5f} secs")
print(f"cython time:\t{cython_end:.5f} secs")