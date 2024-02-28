def verify_digits(str: str) -> int: 
    for i in str:
        if i.isdigit():
            first_number = i
            break
    for i in reversed(str):
        if i.isdigit():
            last_number = i
            break

    result = int(first_number) * 10 + int(last_number)    
    return result

file_path = "/root/repos/Advent-Of-Code/2023/day1_trebuchet/day1.txt"

with open(file_path, "r") as input_file:
    input = []
    for line in input_file:
        line = line[:-1]
        input.append(line)

result = 0
for i in input:
    result += verify_digits(i)

print(result)