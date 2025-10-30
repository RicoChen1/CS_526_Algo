import os

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

def test_single_file(input_file, output_file):
    # test one file and save result
    count = 0
    results = []
    
    # read input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # check each line
    for line in lines:
        line = line.strip()  # clean line, keep spaces inside
        if is_palidrome(line):
            results.append("True")
            count += 1
        else:
            results.append("False")
    
    # write output file
    with open(output_file, 'w') as f:
        for result in results:
            f.write(result + '\n')
        f.write(str(count))  # total count at end, no newline
    
    return count

def run_all_tests():
    # run all test cases
    test_files = [
        "palendrome_0.txt", "palendrome_0S.txt", "palendrome_0L.txt",
        "palendrome_1.txt", "palendrome_1S.txt", "palendrome_1L.txt", 
        "palendrome_2.txt", "palendrome_2S.txt", "palendrome_2L.txt",
        "palendrome_3.txt", "palendrome_3S.txt", "palendrome_3L.txt",
        "palendrome_4.txt", "palendrome_4S.txt", "palendrome_4L.txt"
    ]
    
    for input_file in test_files:
        output_file = "my_" + input_file  # output file name
        try:
            count = test_single_file(input_file, output_file)
            print(f"Test {input_file}: found {count} palindromes -> {output_file}")
        except FileNotFoundError:
            print(f"Skip {input_file}: file not found")  # file not exist

def check_answers():
    # compare my output with answer files
    test_files = ["0", "0S", "0L", "1", "1S", "1L", "2", "2S", "2L", "3", "3S", "3L", "4", "4S", "4L"]
    
    all_correct = True
    for file_id in test_files:
        my_file = f"my_palendrome_{file_id}.txt"
        ans_file = f"palendrome_ans_{file_id}.txt"
        
        try:
            # read both files
            with open(my_file, 'r') as f1, open(ans_file, 'r') as f2:
                my_lines = f1.readlines()
                ans_lines = f2.readlines()
            
            # check if same
            if my_lines == ans_lines:
                print(f"✓ {file_id}: PASS")
            else:
                print(f"✗ {file_id}: FAIL")
                all_correct = False
        except FileNotFoundError:
            print(f"? {file_id}: File not found")
    
    return all_correct

def clean_up():
    # remove all generated test files (like make clean)
    test_files = ["0", "0S", "0L", "1", "1S", "1L", "2", "2S", "2L", "3", "3S", "3L", "4", "4S", "4L"]
    
    removed_count = 0
    for file_id in test_files:
        my_file = f"my_palendrome_{file_id}.txt"
        if os.path.exists(my_file):
            os.remove(my_file)
            print(f"Removed: {my_file}")
            removed_count += 1
    
    print(f"Cleaned up {removed_count} files")

if __name__ == "__main__":
    import sys
    
    # check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "clean":
            clean_up()
        elif sys.argv[1] == "test":
            run_all_tests()
            print("\n" + "="*50 + "\n")
            check_answers()
        else:
            print("Usage: python test_palindrome.py [test|clean]")
    else:
        # default: run tests and check answers
        run_all_tests()
        print("\n" + "="*50 + "\n")
        if check_answers():
            print("\n✔  All tests pass!")
        else:
            print("\n❌ Tests failed!")
        
        print("\nTo clean up generated files, run: python test_palindrome.py clean")
        print("To run tests only, run: python test_palindrome.py test")