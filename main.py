import sys
import time
from subprocess import Popen, PIPE, STDOUT

current_day = 14
run_all = False


def run():
    if run_all:
        start = time.perf_counter()
        for day in range(1, current_day + 1):
            s = time.perf_counter()
            print(f"Day {day}")
            with Popen(f"python day{day}.py", stdout=PIPE, stderr=STDOUT) as p:
                for line in p.stdout:
                    sys.stdout.buffer.write(line)
            elapsed = time.perf_counter() - s
            print(f"Day {day} executed in {elapsed:0.2f} seconds.\n")
        elapsed = time.perf_counter() - start
        print(f"All Days executed in {elapsed:0.2f} seconds.\n")
    else:
        s = time.perf_counter()
        print(f"Day {current_day}")
        with Popen(f"python day{current_day}.py", stdout=PIPE, stderr=STDOUT) as p:
            for line in p.stdout:
                sys.stdout.buffer.write(line)
        elapsed = time.perf_counter() - s
        print(f"Day {current_day} executed in {elapsed:0.2f} seconds.")


if __name__ == "__main__":
    run()
