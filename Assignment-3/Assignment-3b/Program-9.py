class StringProcessor:
    def processString(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            return len(args[0])

        elif len(args) == 2 and isinstance(args[0], str):
            string, operation = args
            if operation.lower() == "upper":
                return string.upper()
            elif operation.lower() == "reverse":
                return string[::-1]
            else:
                return f"Invalid operation: {operation}"

        else:
            return "Invalid arguments passed!"


# Main Program
if __name__ == "__main__":
    sp = StringProcessor()

    text = "Thisismee"

    print("Length:", sp.processString(text))

    print("Uppercase:", sp.processString(text, "upper"))

    print("Reversed:", sp.processString(text, "reverse"))

    print("Invalid Test:", sp.processString(text, "capitalize"))
