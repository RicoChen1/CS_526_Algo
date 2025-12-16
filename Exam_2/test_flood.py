import subprocess
import sys
from typing import List


def run_cmd(cmd: List[str]) -> str:
    """
    Run a command and capture its stdout as text.
    """
    completed = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return completed.stdout


def main() -> None:
    """
    Execute solver on the two provided sample files and print outputs.
    """
    base = r"c:\Users\RicoC\Desktop\BU\CS_526_Algo\Exam_2"
    files = [
        fr"{base}\flood_1.txt",
        fr"{base}\flood_2.txt",
    ]
    for f in files:
        out = run_cmd([sys.executable, r"c:\Users\RicoC\Desktop\BU\CS_526_Algo\Exam_2\flood_solver.py", f])
        print(out.strip())


if __name__ == "__main__":
    main()

