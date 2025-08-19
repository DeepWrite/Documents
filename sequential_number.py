import os
import re

def replace_sequential_numbers(input_file):
    """
    Replace sequential numbers (1, 2, 3, ...) in a file with '[^숫자]' format.
    Args:
        input_file (str): Path to the input file.
    """
    # Ensure the file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Read the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace sequential numbers with '[^숫자]'
    expected_number = 1
    def replace_sequential_number(match):
        nonlocal expected_number
        number = int(match.group())
        if number == expected_number:
            replacement = f"[^{expected_number}]"
            expected_number += 1
            return replacement
        else:
            return match.group()  # Do not replace if not sequential

    # Match numbers, including those right after letters (e.g., 'm10')
    updated_content = re.sub(r"(?<!\d)(?<!\[)\d+", replace_sequential_number, content)

    # Determine the output file path
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}(2){ext}"

    # Save the updated content to the new file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Processed file saved as: {output_file}")

# Main script to interact with the user
if __name__ == "__main__":
    input_file = input("Enter the path of the file to process: ").strip()
    replace_sequential_numbers(input_file)
