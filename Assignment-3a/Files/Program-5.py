def search_keyword(file_path, keyword):
    try:
        keyword_lower = keyword.lower()
        line_numbers = []

        with open(file_path, "r") as f:
            for i, line in enumerate(f, start=1):
                if keyword_lower in line.lower():
                    line_numbers.append(i)

        if line_numbers:
            print("Lines:", ", ".join(map(str, line_numbers)))
        else:
            print("Keyword not found")

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print("An error occurred:", str(e))

file_path = "document.txt"
keyword = input("Enter keyword to search: ")

with open(file_path, "w") as f:
    f.write("Python is great\nI love python\nJava is good\n")

search_keyword(file_path, keyword)