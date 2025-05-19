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

## 🧠 Project Overview

In many applications, pulling structured data from messy text is *essential*. This tool solves that with a clean, reusable, and extensible Python class using **regex patterns**. It’s optimized for common use cases and real-world edge cases.

---

## ✅ Supported Data Types

| Data Type       | Example               | Pattern Snippet                       |                            |
| --------------- | --------------------- | ------------------------------------- | -------------------------- |
| **Email**       | `user@example.com`    | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+...` |                            |
| **URL**         | `https://example.com` | `https?://(?:www\.)?...`              |                            |
| **Phone**       | `(123) 456-7890`      | `\(\d{3}\)...`                        |                            |
| **Credit Card** | `1234 5678 9012 3456` | `\d{4}[\s-]?...`                      |                            |
| **Time**        | `2:30 PM`, `14:30`    | \`(?:0?\[1-9]                         | 1\[0-2]):\[0-5]\[0-9]...\` |
| **HTML Tags**   | `<div class="tag">`   | `<[^>]+>`                             |                            |
| **Hashtags**    | `#RegExRocks`         | `#[a-zA-Z0-9_]+`                      |                            |
| **Currency**    | `$1,234.56`           | `\$\d{1,3}(,\d{3})*(\.\d{2})?`        |                            |

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

# Save to JSON
python regex_cli.py --file sample_input.txt --type all --output results.json
```

---

## 🧪 Testing

Run the test suite:

```bash
python test_regex_extractor.py
```

Covers all patterns and common edge cases ✅

---

## 📁 Project Structure

```
├── regex_extractor.py        # Main regex logic
├── regex_cli.py              # CLI interface
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

---

## ⚠️ Known Limitations

* 📞 Phone: No international formats (yet)
* 💳 Credit Cards: Assumes 16-digit formats
* 💰 Currency: Only USD (\$)
* 🌍 URLs: Only http/https supported
* 🏷 HTML: Simplified matching (not a full parser)

---

## 🔮 Future Enhancements

* 🌐 International phone support
* 💱 More currency formats (€, £, ¥, etc.)
* 📈 Performance boosts for large files
* 🧵 Advanced HTML and URL parsing

---

## 👩🏾‍💻 Author

Created with ❤️ by **Aurore Umumararungu**
For the Software Engineering Program at **African Leadership University**

---

## 📜 License

MIT License – See `LICENSE` file.

---



