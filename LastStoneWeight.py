def main():
    rocks = input("Enter stones weights separated by space: ").strip()
    rocks = [int(x) for x in rocks.split(" ")]
    result = game(rocks)
    print(result)


def game(rocks):
    build_max_heap(rocks)

    while len(rocks) > 1:
        heap_extract_rocks_to_collision(rocks)

    if len(rocks) == 1:
        return rocks[0]

    return 0


def build_max_heap(rocks):
    if len(rocks) % 2 == 0:
        for i in range(int(len(rocks) / 2) + 1, len(rocks) + 1):
            max_heapify(rocks, len(rocks) - i)
    else:
        for i in range(int(len(rocks) / 2) + 2, len(rocks) + 1):
            max_heapify(rocks, len(rocks) - i)


def max_heapify(rocks, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(rocks) and rocks[left] > rocks[i]:
        largest = left
    if right < len(rocks) and rocks[right] > rocks[largest]:
        largest = right
    if largest != i:
        rocks[i], rocks[largest] = rocks[largest], rocks[i]
        max_heapify(rocks, largest)


def heap_extract_rocks_to_collision(rocks):
    max_1 = rocks[0]
    rocks[0] = rocks[len(rocks) - 1]
    del rocks[len(rocks) - 1:len(rocks)]
    max_heapify(rocks, 0)

    max_2 = rocks[0]
    rocks[0] = max_1 - max_2
    max_heapify(rocks, 0)


main()
