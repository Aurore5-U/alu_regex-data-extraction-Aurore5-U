# 📊 RegEx Data Extraction Tool

A Python tool to extract useful data from text using **regular expressions**.

This project identifies and extracts:

* 📧 Emails
* 🌐 URLs
* 📞 Phone numbers
* 💳 Credit card numbers
* ⏰ Time formats (12/24 hr)
* 🔖 HTML tags
* 🏷 Hashtags
* 💵 Currency values

---


## ⚙️ Installation

```bash
git clone https://github.com/your-username/alu_regex-data-extraction-username.git
cd alu_regex-data-extraction-username
```

> No external libraries needed – just Python’s standard `re` module!

---

## 🚀 Usage

### 1. Python Module

```python
from regex_extractor import RegexExtractor

text = """
Contact support@example.com or visit https://www.example.com.
Call (123) 456-7890. Card: 1234-5678-9012-3456.
Meeting at 2:30 PM. <div class="note">Hi!</div>
#StaySafe $19.99
"""

extractor = RegexExtractor()

emails = extractor.extract_emails(text)
print(emails)

all_data = extractor.extract_all(text)
for category, items in all_data.items():
    print(f"{category}: {items}")
```

### 2. Command-Line Tool

```bash
# Extract emails
python regex_cli.py --file sample_input.txt --type email

# Extract all types
python regex_cli.py --text "user@example.com (123) 456-7890" --type all


## 🧪 Testing

Run the test suite:

```bash
python main.py
```

Covers all patterns and common edge cases ✅

---

## 📁 Project Structure

```
├── regex_extractor.py        # Main regex logic
├── sample_input.txt          # Demo text input
├── test_regex_extractor.py   # Unit tests
├── main.py                   # Example script
└── README.md                 # You're here!
```

---

## 🧩 Edge Case Coverage

This tool is built with common real-world patterns in mind:

* ✅ Email subdomains, weird TLDs
* ✅ URLs with subdomains/paths
* ✅ Phone formats: (123), 123-456-7890, 123.456.7890
* ✅ 12/24-hour time, AM/PM
* ✅ Credit card spacing/hyphens
* ✅ CamelCase and *underscored* hashtags
* ✅ Currency with/without commas or decimals

## 👩🏾‍💻 Author

Created with ❤️ by **Aurore Umumararungu**
For the Software Engineering Program at **African Leadership University**

---

## 📜 License

MIT License 

---



