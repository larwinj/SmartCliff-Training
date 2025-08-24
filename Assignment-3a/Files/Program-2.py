def reverse_file_content(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()

        reversed_lines = [line.strip()[::-1] for line in reversed(lines)]

        # Write to output file
        with open(output_file, "w") as f:
            for line in reversed_lines:
                f.write(line + "\n")

        print(f"Reversed content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print("An error occurred:", str(e))


input_file = "sample1.txt"
output_file = "reversed.txt"

with open(input_file, "w") as f:
    f.write("Hello\nWorld\nPython\nRocks")

reverse_file_content(input_file, output_file)

with open(output_file, "r") as f:
    print(f.read())
