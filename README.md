# CS 526 - Assignment 1: Hello World


### How to Run

1.  Create an input file (e.g., `myfile.txt`) with some content:
    ```
    Hello from Y.Chen
    ```

2.  In your terminal, run one of the following commands:

    **PowerShell:**
    ```powershell
    Get-Content myfile.txt | python helloworld.py
    ```

    **CMD:**
    ```bash
    python helloworld.py < myfile.txt
    ```

3.  The script will output the content of the file.