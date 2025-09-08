def split_file(input_file, lines_per_file):
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        total_lines = len(lines)
        file_count = 1

        for i in range(0, total_lines, lines_per_file):
            part_lines = lines[i:i + lines_per_file]
            output_file = f"part{file_count}.txt"
            with open(output_file, "w") as out:
                out.writelines(part_lines)
            print(f"{output_file} created with lines {i+1}-{i+len(part_lines)}")
            file_count += 1

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print("An error occurred:", str(e))


input_file = "bigfile.txt"
N = int(input("Enter the maximum number of lines per file: "))

with open(input_file, "w") as f:
    f.write("Hi\nHello\nHow\nAre\nYou\nBoys\n")

split_file(input_file, N)
