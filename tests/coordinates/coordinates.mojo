import random
import time


def _perf_counter() -> Float64:
    let _time = time.now()
    return _time / 1000000000


def _generate_objects(
    start_pos_x: Float64,
    start_pos_y: Float64,
    count: Int,
) -> object:
    let objects: object = []

    for obj in range(count):
        let pos_x = start_pos_x + random.random_float64(0.0, 999999.0) / 1000000
        let pos_y = start_pos_y + random.random_float64(0.0, 999999.0) / 1000000
        objects.append([pos_x, pos_y])

    return objects


def _calculate_shape_points(
    pos1: object,
    pos2: object,
) -> object:
    let pos1_x = pos1.__getitem__(0)
    let pos1_y = pos1.__getitem__(1)

    let pos2_x = pos2.__getitem__(0)
    let pos2_y = pos2.__getitem__(1)

    let pos3_x = pos1_x
    let pos3_y = pos2_y

    let pos4_x = pos2_x
    let pos4_y = pos1_y

    let pos3 = [pos3_x, pos3_y]
    let pos4 = [pos4_x, pos4_y]

    let shape_points = [pos1, pos2, pos3, pos4]
    return shape_points


def _search_objects(
    objects: object,
    shape: object,
) -> object:
    let founded_objects: object = []

    let pos1 = shape.__getitem__(0)
    let pos2 = shape.__getitem__(1)
    let pos3 = shape.__getitem__(2)
    let pos4 = shape.__getitem__(3)

    let pos1_x = pos1.__getitem__(0)
    let pos1_y = pos1.__getitem__(1)

    let pos2_x = pos2.__getitem__(0)
    let pos2_y = pos2.__getitem__(1)

    let _objects = ListLiteral(objects).__len__()

    for count in range(_objects):
        let _obj = objects.__getitem__(count)
        let pos_x = _obj.__getitem__(0)
        let pos_y = _obj.__getitem__(1)

        if pos_x >= pos2_x and pos_x <= pos1_x and pos_y >= pos1_y and pos_y <= pos2_y:
            founded_objects.append(_obj)

    return founded_objects


fn perf_counter() -> Float64:
    let _time: Int = time.now()
    return _time / 1000000000


# fn generate_objects(
#     start_pos_x: Float64,
#     start_pos_y: Float64,
#     count: Int,
# ) raises -> ListLiteral[ListLiteral[Float64, Float64]]:
#     var objects: object = []

#     for obj in range(count):
#         let pos_x: Float64 = (start_pos_x + random.random_float64(0.0, 999999.0) / 1000000.0)
#         let pos_y: Float64 = (start_pos_y + random.random_float64(0.0, 999999.0) / 1000000.0)
#         objects.append([pos_x, pos_y])

#     let _objects = ListLiteral(objects)
#     return _objects


# fn calculate_shape_points(
#     pos1: ListLiteral[Float64],
#     pos2: ListLiteral[Float64],
# ) raises -> ListLiteral[ListLiteral[Float64]]:
#     let pos1_x: Float64 = pos1.get[0, Float64]
#     let pos1_y: Float64 = pos1.get[1, Float64]

#     let pos2_x: Float64 = pos2.get[0, Float64]
#     let pos2_y: Float64 = pos2.get[1, Float64]

#     let pos3_x: Float64 = pos1_x
#     let pos3_y: Float64 = pos2_y

#     let pos4_x: Float64 = pos2_x
#     let pos4_y: Float64 = pos1_y

#     let pos3: ListLiteral[Float64] = [pos3_x, pos3_y]
#     let pos4: ListLiteral[Float64] = [pos4_x, pos4_y]

#     let shape_points: ListLiteral[Float64] = [pos1, pos2, pos3, pos4]
#     return shape_points


# fn search_objects(
#     objects: ListLiteral[Float64],
#     shape: ListLiteral[ListLiteral[Float64]],
# ) raises -> ListLiteral[ListLiteral[Float64]]:
#     let founded_objects: ListLiteral

#     let pos1: ListLiteral[Float64] = shape.get[0, ListLiteral[Float64, Float64]]
#     let pos2: ListLiteral[Float64] = shape.get[1, ListLiteral[Float64, Float64]]
#     let pos3: ListLiteral[Float64] = shape.get[2, ListLiteral[Float64, Float64]]
#     let pos4: ListLiteral[Float64] = shape.get[3, ListLiteral[Float64, Float64]]

#     let pos1_x: Float64 = pos1.get[0, Float64]
#     let pos1_y: Float64 = pos1.get[1, Float64]

#     let pos2_x: Float64 = pos2.get[0, Float64]
#     let pos2_y: Float64 = pos2.get[1, Float64]

#     for obj in objects:
#         let pos_x: Float64 = obj.get[0, Float64]
#         let pos_y: Float64 = obj.get[1, Float64]

#         if pos_x >= pos2_x and pos_x <= pos1_x and pos_y >= pos1_y and pos_y <= pos2_y:
#             founded_objects.append(obj)

#     return founded_objects


fn main():
    try:
        let _mojo_start = perf_counter()
        let _pos1 = object([55.767351, 37.558771])
        let _pos2 = object([55.761848, 37.570799])
        let _objects_start = perf_counter()
        let _objects = _generate_objects(
            start_pos_x=55.000000,
            start_pos_y=37.000000,
            count=5_000,
        )
        let _objects_end = perf_counter() - _objects_start
        let _shape_start = perf_counter()
        let _pos_points = _calculate_shape_points(_pos1, _pos2)
        let _shape_end = perf_counter() - _shape_start
        let _search_start = perf_counter()
        let _founded_objects = _search_objects(_objects, _pos_points)
        let _search_end = perf_counter() - _search_start
        let mojo_end: Float64 = perf_counter() - _mojo_start
        print("EXECUTION TIME")
        print("mojo time:\t", mojo_end, "secs")
    except Error:
        pass

    # let mojo_start: Float64 = perf_counter()
    # let pos1: ListLiteral[Float64] = [55.767351, 37.558771]
    # let pos2: ListLiteral[Float64] = [55.761848, 37.570799]
    # let objects_start: Float64 = perf_counter()
    # let objects: ListLiteral[ListLiteral[Float64]] = generate_objects(
    #     start_pos_x=55.000000,
    #     start_pos_y=37.000000,
    #     count=5_000,
    # )
    # let objects_end: Float64 = perf_counter() - objects_start
    # let shape_start: Float64 = perf_counter()
    # let pos_points: ListLiteral[ListLiteral[Float64]] = calculate_shape_points(
    #     pos1, pos2
    # )
    # let shape_end: Float64 = perf_counter() - shape_start
    # let search_start: Float64 = perf_counter()
    # let founded_objects: ListLiteral[ListLiteral[Float64]] = search_objects(
    #     objects, pos_points
    # )
    # let search_end: Float64 = perf_counter() - search_start
    # let mojo_end: Float64 = perf_counter() - mojo_start
    # print("EXECUTION TIME")
    # print("mojo time:\t", mojo_end, "secs")
