def find_and_replace(file_path, old_text, new_text):
    try:
        # Read the file content
        with open(file_path, "r") as file:
            content = file.read()

        # Replacing
        updated_content = content.replace(old_text, new_text)

        # Write the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)

        print("Text replaced successfully!")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


file_name = "sample1.txt"

with open(file_name, "w") as f:
    f.write("Hello, World! This is a test file.")

find_and_replace(file_name, "World", "Python")
find_and_replace(file_name, "test", "sample")

with open(file_name, "r") as f:
    print("Updated File Content:", f.read())
