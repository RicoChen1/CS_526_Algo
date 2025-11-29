import sys
from typing import List, Tuple, Optional


def parse_input(path: str) -> Tuple[List[int], List[int]]:
    # read A and B arrays from file
    with open(path, 'r', encoding='utf-8') as f:
        la = int(f.readline().strip())
        lb = int(f.readline().strip())
        A = list(map(int, f.readline().strip().split()))
        B = list(map(int, f.readline().strip().split()))
    return A, B


def longest_alternating_increasing(A: List[int], B: List[int]) -> List[int]:
    # DP optimized to O(n*m) with prefix maxima, plus backtracking
    n, m = len(A), len(B)
    if n == 0 or m == 0:
        return []

    fA = [[0] * m for _ in range(n)]  # end at A[i], previous was B[j]
    fB = [[0] * m for _ in range(n)]  # end at B[j], previous was A[i]
    backA: List[List[Optional[Tuple]] ] = [[None] * m for _ in range(n)]
    backB: List[List[Optional[Tuple]] ] = [[None] * m for _ in range(n)]

    # prefix max over i for fB[*][j]: preB[i][j] = max_{k < i} fB[k][j]
    preB = [[0] * m for _ in range(n + 1)]
    idxPreB = [[-1] * m for _ in range(n + 1)]  # argmax k for preB

    best = (0, 'A', 0, 0)

    for i in range(n):
        running_max = 0
        running_idx = -1
        # preA[i][j] = max_{l < j} fA[i][l]
        for j in range(m):
            preA_val = running_max
            preA_idx = running_idx

            # compute fA using preB
            if A[i] > B[j]:
                best_len = 2
                best_prev: Tuple = ('SB', j)
                if preB[i][j] + 1 > best_len:
                    k = idxPreB[i][j]
                    if k != -1:
                        best_len = preB[i][j] + 1
                        best_prev = ('B', k, j)
                fA[i][j] = best_len
                backA[i][j] = best_prev

            # compute fB using row prefix of fA
            if B[j] > A[i]:
                best_len = 2
                best_prev: Tuple = ('SA', i)
                if preA_val + 1 > best_len:
                    l = preA_idx
                    if l != -1:
                        best_len = preA_val + 1
                        best_prev = ('A', i, l)
                fB[i][j] = best_len
                backB[i][j] = best_prev

            # update row prefix for fA
            if fA[i][j] > running_max:
                running_max = fA[i][j]
                running_idx = j

            # track global best
            if fA[i][j] > best[0]:
                best = (fA[i][j], 'A', i, j)
            if fB[i][j] > best[0]:
                best = (fB[i][j], 'B', i, j)

        # update column prefix for fB to next i+1
        for j in range(m):
            if fB[i][j] >= preB[i][j]:
                preB[i + 1][j] = fB[i][j]
                idxPreB[i + 1][j] = i
            else:
                preB[i + 1][j] = preB[i][j]
                idxPreB[i + 1][j] = idxPreB[i][j]

    if best[0] == 0:
        return []

    # reconstruct sequence
    seq: List[int] = []
    typ, i, j = best[1], best[2], best[3]
    while True:
        if typ == 'A':
            seq.append(A[i])
            prev = backA[i][j]
            if prev is None:
                break
            if prev[0] == 'B':
                typ, i, j = 'B', prev[1], prev[2]
                continue
            if prev[0] == 'SB':
                seq.append(B[prev[1]])
                break
        else:
            seq.append(B[j])
            prev = backB[i][j]
            if prev is None:
                break
            if prev[0] == 'A':
                typ, i, j = 'A', prev[1], prev[2]
                continue
            if prev[0] == 'SA':
                seq.append(A[prev[1]])
                break

    seq.reverse()
    return seq


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python longest_seq.py <input_file>")
        return
    path = sys.argv[1]
    A, B = parse_input(path)
    seq = longest_alternating_increasing(A, B)
    base = path.replace('\\', '/').split('/')[-1]
    print(f"File Input: {base}")
    print("Longest Sequence:", " ".join(map(str, seq)))


if __name__ == "__main__":
    main()
