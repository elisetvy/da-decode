def decode(message_file):
    with open(message_file, 'r') as file:
        lines = [line.rstrip('\n') for line in file]

    sorted_lines = sorted(lines, key=lambda x: int(x.split()[0]))
    stairs = create_staircase(sorted_lines)

    message = ""

    for stair in stairs:
        message += stair[-1].split()[1] + " "

    return message.strip()


def create_staircase(nums):
    step = 1
    subsets = []
    while nums:
        if len(nums) >= step:
            subset = nums[:step]
            subsets.append(subset)
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets

input_file_path = "coding_qual_input.txt"
decoded_message = decode(input_file_path)
print(decoded_message)