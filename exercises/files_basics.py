from pathlib import Path

practice_path = Path(__file__).parent / "practice.txt"
with open(practice_path, "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("This is a practice file.\n")
    f.write("We are learning how to work with files in Python.\n")

with open(practice_path, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        print(line_number, line.strip())

print(practice_path.exists())
print(practice_path.resolve())