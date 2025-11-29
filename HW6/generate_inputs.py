import random

def generate_file(filename, count, max_val=1000):
    with open(filename, 'w') as f:
        numbers = [str(random.randint(1, max_val)) for _ in range(count)]
        f.write(' '.join(numbers))
    print(f"Generated {filename} with {count} numbers.")

if __name__ == "__main__":
    generate_file('HW6/input_small.txt', 15)
    generate_file('HW6/input_medium.txt', 50)
    generate_file('HW6/input_large.txt', 500)
