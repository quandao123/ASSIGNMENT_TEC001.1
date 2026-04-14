# 1. 
def count_lines(filepath):
    with open(filepath) as f:
        return sum(1 for line in f if line.strip())


# 2.
def find_keyword_lines(filepath, keyword):
    with open(filepath) as f:
        return [i + 1 for i, line in enumerate(f) if keyword in line]


# 3. 
def to_uppercase(filepath):
    with open(filepath) as f:
        content = f.read()
    with open("output.txt", "w") as f:
        f.write(content.upper())


# 4.
def average_score(filepath):
    with open(filepath) as f:
        scores = [int(line.split(",")[1]) for line in f if line.strip()]
    return sum(scores) / len(scores)
