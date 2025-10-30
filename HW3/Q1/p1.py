def is_palidrome(s): 
    # Remove spaces and convert to lowercase for comparison
    s_clean = s.replace(' ', '').lower()
    left = 0
    right = len(s_clean) - 1  # tail of string

    while left < right:
        if s_clean[left] != s_clean[right]:  # char dont match, not 回文
            return False 
        left += 1
        right -= 1
    return True

def main():
    count = 0
    # read a file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()  # clean line,but keep spaces inside
        if is_palidrome(line):
            print("True")
            count += 1
        else:
            print("False")

    print(count, end="")  # total count output

if __name__ == "__main__":
    main()  # run main function