import sys
import time
def loading_dots():
    loading = True  # a simple var to keep the loading status
    loading_speed = 4  # number of characters to print out per second
    loading_string = "." * 6  # characters to print out one by one (6 dots in this example)
    for index, char in enumerate(loading_string):
        # you can check your loading status here
        sys.stdout.write(char)  # write the next char to STDOUT
        sys.stdout.flush()  # flush the output
        time.sleep(1.0 / loading_speed)  # wait to match our speed
    index += 1  # lists are zero indexed, we need to increase by one for the accurate count
    # backtrack the written characters, overwrite them with space, backtrack again:
    sys.stdout.write("\b" * index + " " * index + "\b" * index)
    sys.stdout.flush()  # flush the output
