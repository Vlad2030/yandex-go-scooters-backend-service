#include <iostream>
#include <vector>
#include <chrono>
#include <ctime>
#include <cstdlib>
#include <iomanip>

std::vector<std::vector<float>> generateObjects(
    float start_pos_x, float start_pos_y, int count) {
    std::vector<std::vector<float>> objects;

    for (int obj = 0; obj < count; obj++) {
        float pos_x = start_pos_x + (rand() % 1000000) / 1000000.0f;
        float pos_y = start_pos_y + (rand() % 1000000) / 1000000.0f;
        objects.push_back({pos_x, pos_y});
    }

    return objects;
}

std::vector<std::vector<float>> calculateShapePoints(
    const std::vector<float>& pos1, const std::vector<float>& pos2) {
    float pos1_x = pos1[0];
    float pos1_y = pos1[1];
    float pos2_x = pos2[0];
    float pos2_y = pos2[1];

    float pos3_x = pos1_x;
    float pos3_y = pos2_y;

    float pos4_x = pos2_x;
    float pos4_y = pos1_y;

    std::vector<float> pos3 = {pos3_x, pos3_y};
    std::vector<float> pos4 = {pos4_x, pos4_y};

    std::vector<std::vector<float>> shapePoints = {pos1, pos2, pos3, pos4};
    return shapePoints;
}

std::vector<std::vector<float>> searchObjects(
    const std::vector<std::vector<float>>& objects,
    const std::vector<std::vector<float>>& shape) {
    std::vector<std::vector<float>> foundObjects;

    float pos1_x = shape[0][0];
    float pos1_y = shape[0][1];
    float pos2_x = shape[1][0];
    float pos2_y = shape[1][1];

    for (const auto& obj : objects) {
        float pos_x = obj[0];
        float pos_y = obj[1];

        if (pos_x >= pos2_x && pos_x <= pos1_x &&
            pos_y >= pos1_y && pos_y <= pos2_y) {
            foundObjects.push_back(obj);
        }
    }

    return foundObjects;
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    std::vector<float> pos1 = {55.767351, 37.558771};
    std::vector<float> pos2 = {55.761848, 37.570799};

    auto pythonStart = std::chrono::high_resolution_clock::now();

    int count = 500000;
    std::vector<std::vector<float>> objects = generateObjects(55.0f, 37.0f, count);

    auto objectsStart = std::chrono::high_resolution_clock::now();
    auto objectsEnd = std::chrono::duration_cast<std::chrono::microseconds>(objectsStart - pythonStart);

    std::vector<std::vector<float>> posPoints = calculateShapePoints(pos1, pos2);
    auto shapeEnd = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - objectsStart);

    auto searchStart = std::chrono::high_resolution_clock::now();
    std::vector<std::vector<float>> foundedObjects = searchObjects(objects, posPoints);
    auto searchEnd = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - searchStart);

    std::cout << "GENERATION TIME" << std::endl;
    std::cout << "objects time:\t" << std::fixed << std::setprecision(6) << objectsEnd.count() / 1000000.0 << " secs" << std::endl;
    std::cout << "shape time:\t" << std::fixed << std::setprecision(6) << shapeEnd.count() / 1000000.0 << " secs" << std::endl;
    std::cout << "search time:\t" << std::fixed << std::setprecision(6) << searchEnd.count() / 1000000.0 << " secs" << std::endl;
    std::cout << std::endl;

    std::cout << "SEARCH POS" << std::endl;
    std::cout << "pos1:\t" << pos1[0] << ", " << pos1[1] << std::endl;
    std::cout << "pos2:\t" << pos2[0] << ", " << pos2[1] << std::endl;
    std::cout << std::endl;

    std::cout << "SHAPE" << std::endl;
    for (int number = 0; number < posPoints.size(); number++) {
        std::cout << "pos" << number + 1 << ":\t" << posPoints[number][0] << ", " << posPoints[number][1] << std::endl;
    }
    std::cout << std::endl;

    std::cout << "OBJECTS: " << objects.size() << std::endl;
    if (objects.size() <= 20) {
        for (int number = 0; number < objects.size(); number++) {
            std::cout << number + 1 << ".\tobj:\t" << objects[number][0] << ", " << objects[number][1] << std::endl;
        }
    }
    std::cout << std::endl;

    std::cout << "FOUNDED OBJECTS (" << foundedObjects.size() << ")" << std::endl;
    if (foundedObjects.size() <= 20) {
        for (int number = 0; number < foundedObjects.size(); number++) {
            std::cout << number + 1 << ".\tobj:\t" << foundedObjects[number][0] << ", " << foundedObjects[number][1] << std::endl;
        }
    }

    auto pythonEnd = std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::high_resolution_clock::now() - pythonStart);
    std::cout << std::endl;
    std::cout << "EXECUTION TIME" << std::endl;
    std::cout << "C++ time:\t" << std::fixed << std::setprecision(6) << pythonEnd.count() / 1000000.0 << " secs" << std::endl;

    return 0;
}
