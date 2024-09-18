from sys import argv
import time

script, filename = argv
def wait():
    time.sleep(1) # Time in seconds

print(f"We're going to erase {filename}.")
print("If you don't want that, his CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
newLine = ("\n")

print("Opening and truncating the file", end='')
# Print dots on the same line with waits
for _ in range(5):
    print(".", end='', flush=True)
    wait()
target = open(filename, 'w')
print(f"{newLine}File truncated. Goodbye.")
wait()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file")
# Print dots on the same line with waits
for _ in range(5):
    print(".", end='', flush=True)
    wait()
target.write(f"{line1}{newLine}{line2}{newLine}{line3}{newLine}")
print(f"{newLine}Done.")

print(f"{newLine}And finally, we close it. Goodbye.")
wait()
target.close()