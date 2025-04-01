# Last Stone Weight - Max Heap Simulation

## Overview

This Python script simulates a stone-smashing game based on a classic algorithmic problem. Each turn, the two heaviest stones are smashed together:

- If they are equal, both are destroyed.
- If they are unequal, the heavier one is reduced by the weight of the lighter one, and the result is added back.

The process continues until one or no stones remain.

This version uses a custom max heap implementation.

---

## Usage

1. Run the script:
   ```bash
   python main.py
   ```

2. When prompted, enter a space-separated list of stone weights:
   ```
   Enter stones weights separated by space: 2 7 4 1 8 1
   ```

3. Output will be the weight of the last remaining stone (or `0` if all stones are destroyed).

---

## Example

**Input:**
```
2 7 4 1 8 1
```

**Simulation steps:**
- Smash 8 and 7 → 1
- Smash 4 and 2 → 2
- Smash 2 and 1 → 1
- Smash 1 and 1 → 0

**Output:**
```
1
```

---

## Implementation Notes

- A custom **max heap** is implemented using a list and the `max_heapify` function.
- `build_max_heap()` prepares the initial heap.
- `heap_extract_rocks_to_collision()` extracts the two heaviest stones and simulates the collision.

---

## License

This project is released under the MIT License.