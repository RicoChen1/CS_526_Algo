import sys
import re


# map vowels to International Morse code
VOWEL_CODES = {
    'A': '.-',
    'E': '.',
    'I': '..',
    'O': '---',
    'U': '..-'
}


def count_vowel_sequences(s: str) -> int:
    # DP count ways to split s into vowel codes
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    codes = list(VOWEL_CODES.values())
    for i in range(n):
        if dp[i] == 0:
            continue
        for code in codes:
            L = len(code)
            if i + L <= n and s[i:i + L] == code:
                dp[i + L] += dp[i]
    return dp[n]


def main() -> None:
    # read input file path from argv
    if len(sys.argv) < 2:
        print("usage: python vowel_morse.py <input_file>")
        return
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        first = f.readline().strip()
        seq = f.readline().strip()

    # optional: validate length line
    try:
        expected_len = int(first)
    except ValueError:
        expected_len = None

    if expected_len is not None and expected_len != len(seq):
        pass  # length mismatch ignored, we count by actual string length

    total = count_vowel_sequences(seq)

    # build required file label
    base = path.replace('\\', '/').split('/')[-1]
    m = re.search(r"vowel_input(\d+)\.txt", base)
    label = f"vowel_input{m.group(1)}.txt" if m else base

    # required output format
    print(f"File Input: {label}")
    print(f"The Number of Vowel combinations is:  {total}")


if __name__ == "__main__":
    # simple runner
    main()

