def remove_duplicate_lines(input_file, output_file):
    seen = set()
    unique_lines = []

    try:
        with open(input_file, "r") as f:
            for line in f:
                clean_line = line.strip()
                lower_line = clean_line.lower()
                if lower_line not in seen:
                    seen.add(lower_line)
                    unique_lines.append(clean_line)

        with open(output_file, "w") as f:
            for line in unique_lines:
                f.write(line + "\n")

        print(f"Cleaned content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print("An error occurred:", str(e))


input_file = "sample1.txt"
output_file = "cleaned.txt"

with open(input_file, "w") as f:
    f.write("Hello\nWorld\nhello\nPython\nTest\nTest\nTest")

remove_duplicate_lines(input_file, output_file)

with open(output_file, "r") as f:
    print(f.read())
