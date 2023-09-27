# mycode.pyx
import cython
cimport numpy as cnp
import numpy as np
from cython.parallel import prange
import time
cimport libc.stdlib
from libc.math cimport sqrt

cpdef generate_objects(int start_pos_x, int start_pos_y, int count):
    cdef int obj
    cdef double pos_x, pos_y
    cdef cnp.ndarray[cnp.float64_t, ndim=2] objects = np.empty((count, 2), dtype=np.float64)
    cdef double[:, :] objects_view = objects

    with nogil:
        for obj in prange(count):
            pos_x = start_pos_x + libc.stdlib.rand() / 1000000.0
            pos_y = start_pos_y + libc.stdlib.rand() / 1000000.0
            objects_view[obj, 0] = pos_x
            objects_view[obj, 1] = pos_y

    cdef list result = [[objects_view[i, 0], objects_view[i, 1]] for i in range(count)]
    return result


@cython.boundscheck(False)
@cython.wraparound(False)
def calculate_shape_points(cnp.ndarray[cnp.float64_t, ndim=1] pos1, cnp.ndarray[cnp.float64_t, ndim=1] pos2):
    cdef cnp.ndarray[cnp.float64_t, ndim=1] result = np.empty(4, dtype=np.float64)
    result[0] = pos1[0]
    result[1] = pos1[1]
    result[2] = pos2[0]
    result[3] = pos2[1]

    return result


def search_objects(
        objects,
        shape,
):
    cdef float pos1_x, pos1_y, pos2_x, pos2_y, pos_x, pos_y
    cdef list founded_objects

    pos1_x, pos1_y = shape[0]
    pos2_x, pos2_y = shape[1]

    founded_objects = []

    for obj in objects:
        pos_x, pos_y = obj

        if (pos_x >= pos2_x and pos_x <= pos1_x
                and pos_y >= pos1_y and pos_y <= pos2_y):
            founded_objects.append(obj)

    return founded_objects


pos1 = np.array([55.767351, 37.558771], dtype=np.float64)
pos2 = np.array([55.761848, 37.570799], dtype=np.float64)

def main():
    objects_start = time.perf_counter()
    objects = generate_objects(
        start_pos_x=55,
        start_pos_y=37,
        count=50_000,
    )
    objects_end = time.perf_counter() - objects_start

    shape_start = time.perf_counter()
    pos_points = calculate_shape_points(pos1, pos2)
    shape_end = time.perf_counter() - shape_start

    search_start = time.perf_counter()
    founded_objects = search_objects(objects, [list(pos1), list(pos2)])
    search_end = time.perf_counter() - search_start

    print("GENERATION TIME")
    print(f"objects time:\t{objects_end:.5f} secs")
    print(f"shape time:\t{shape_end:.5f} secs")
    print(f"search time:\t{search_end:.5f} secs")
    print()
    print("SEARCH POS")
    print(f"pos1:\t{pos1}")
    print(f"pos2:\t{pos2}")
    print()
    print("SHAPE")
    for number, point in enumerate(pos_points, 1):
        print(f"pos{number}:\t{point}")
    print()
    print(f"OBJECTS: {len(objects)}")
    if len(objects) <= 20:
        for number, obj in enumerate(objects, 1):
            print(f"{number}.\tobj:\t{obj}")
    print()
    print(f"FOUNDED OBJECTS ({len(founded_objects)})")
    if len(founded_objects) <= 20:
        for number, obj in enumerate(founded_objects, 1):
            print(f"{number}.\tobj:\t{obj}")

if __name__ == "__main__":
    main()
