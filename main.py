import os
from regex_extractor import RegexExtractor

def main():
    extractor = RegexExtractor()

    # Get the path to the input file
    file_path = 'sample_input.txt'

    # Try to read the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Using sample text instead.")
        text = """
        Email: user@example.com
        Website: https://www.example.com
        Phone: 123-456-7890
        Credit Card: 1234 5678 9012 3456
        Time: 14:30 or 2:30 PM
        Tag: <p>Sample</p>
        Hashtag: #Example
        Price: $19.99
        """

    # Extract data
    results = extractor.extract_all(text)

    # Print the results
    print("\n--- Extracted Data ---")
    for category, items in results.items():
        print(f"\n{category.title()}:")
        for item in items:
            print(f"  - {item}")

if __name__ == "__main__":
    main()

