import sys
import heapq
from typing import List, Tuple, Optional


"""
    Parse input lines:
    - n: num of cracks
    - threshold: flood threshold
    - drain: water drained per time
    - cracks: list of (appearance_time, initial_size), sort by time
"""
def parse_input(lines: List[str]) -> Tuple[int, int, int, List[Tuple[int, int]]]:
    it = iter(lines)
    n = int(next(it).strip())
    threshold = int(next(it).strip())
    drain = int(next(it).strip())
    cracks: List[Tuple[int, int]] = []
    for _ in range(n):
        t_s = next(it).strip().split()
        t = int(t_s[0])
        s = int(t_s[1])
        cracks.append((t, s))
    # Input is guaranteed non-decreasing by time; keep as-is
    return n, threshold, drain, cracks


"""
    Simulate process and return:
    - status: "SAFE" or "FLOOD"
    - time_of_evacuate: time when evacuation is triggered (None if SAFE)
    - water_at_event: floodwater units when flooding occurred (0 if SAFE)
    - max_water: maximum floodwater ever reached
"""
def simulate_flood(n: int, threshold: int, drain: int, cracks: List[Tuple[int, int]]) -> Tuple[str, Optional[int], int, int]:

    # Max-heap via heapq with negative values; we store "stored = actual_size - delta"
    heap: List[int] = []
    sum_stored = 0  # sum of all stored values in heap (actual sizes can be recovered by + delta)
    delta = 0  # global growth applied to all unfixed cracks
    W = 0  # current water in the village
    t_cur = 0  # current time
    i = 0  # index into cracks
    max_water = 0  # track the maximum floodwater ever reached

    while i < n or heap:
        # If there are no active cracks, jump to next crack's appearance time
        if not heap and i < n and t_cur < cracks[i][0]:
            next_t = cracks[i][0]
            gap = next_t - t_cur
            # During gap, inflow is 0, only drain apply
            # Water decreases by drain * gap but cant below zero
            W = max(0, W - drain * gap)
            t_cur = next_t

        # Add all cracks appear @ current time
        while i < n and cracks[i][0] == t_cur:
            s0 = cracks[i][1]
            stored = s0 - delta  # store base value, without keep add +delta
            heapq.heappush(heap, -stored)  # max-heap by push negative
            sum_stored += stored
            i += 1

        # Fix one crack if any exist (greedy: fix current largest)
        if heap:
            stored_max = -heapq.heappop(heap)
            sum_stored -= stored_max

        # Compute inflow from all remaining cracks
        m = len(heap)
        inflow = sum_stored + m * delta
        W = W + inflow - drain
        if W < 0:
            W = 0
        if W > max_water:
            max_water = W
        if W >= threshold:
            return "FLOOD", t_cur, W, max_water

        # End of time unit: all unfixed cracks grow by +1 (handled by delta)
        delta += 1
        t_cur += 1

    return "SAFE", None, 0, max_water

"""
    Read an input file, simulate, and return a user-friendly string.
"""
def run_on_file(path: str) -> str:

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    n, threshold, drain, cracks = parse_input(lines)
    status, t_ev, w_ev, w_max = simulate_flood(n, threshold, drain, cracks)
    if status == "SAFE":
        return f"SAFE\n{w_max}"
    else:
        return f"FLOOD\n{t_ev}\n{w_ev}"


def main(argv: List[str]) -> None:
    """
    - python Exam_2/flood_solver.py <input_file_path>
    will print result
    """
    if len(argv) == 2:
        path = argv[1]
        print(run_on_file(path))
    else:
        # Read from stdin
        lines = sys.stdin.read().strip().splitlines()
        n, threshold, drain, cracks = parse_input(lines)
        status, t_ev, w_ev, w_max = simulate_flood(n, threshold, drain, cracks)
        if status == "SAFE":
            print("SAFE")
            print(w_max)
        else:
            print("FLOOD")
            print(t_ev)
            print(w_ev)


if __name__ == "__main__":
    main(sys.argv)

