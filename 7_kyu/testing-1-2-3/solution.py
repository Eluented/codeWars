def number(lines):
    return [f"{x}: {lines[x-1]}" for x in range(1, len(lines)+1 )] ##one liner list comprehension used the format with f which just returns the range index that starts at 1 and i somehow made it work my brain hurts
