import re
from typing import List, Dict

class RegexExtractor:
    """
    Extract various types of data using regular expressions:
    - Emails
    - URLs
    - Phone numbers
    - Credit cards
    - Time formats
    - HTML tags
    - Hashtags
    - Currency amounts
    """

    def __init__(self):
        self.patterns = {
            'email': re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'),
            'url': re.compile(r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'),
            'phone': re.compile(r'(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]?\d{4}'),
            'credit_card': re.compile(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'),
            'time': re.compile(r'\b(?:(?:0?[1-9]|1[0-2]):[0-5][0-9]\s*(?:AM|PM|am|pm)|(?:[01]?[0-9]|2[0-3]):[0-5][0-9])\b'),
            'html_tag': re.compile(r'<[^>\s]+[^>]*>'),
            'hashtag': re.compile(r'#[a-zA-Z][a-zA-Z0-9_]*'),
            'currency': re.compile(r'\$(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d{2})?')
        }

    def extract_emails(self, text: str) -> List[str]:
        return self.patterns['email'].findall(text)

    def extract_urls(self, text: str) -> List[str]:
        return self.patterns['url'].findall(text)

    def extract_phone_numbers(self, text: str) -> List[str]:
        return self.patterns['phone'].findall(text)

    def extract_credit_cards(self, text: str) -> List[str]:
        return self.patterns['credit_card'].findall(text)

    def extract_times(self, text: str) -> List[str]:
        return self.patterns['time'].findall(text)

    def extract_html_tags(self, text: str) -> List[str]:
        return self.patterns['html_tag'].findall(text)

    def extract_hashtags(self, text: str) -> List[str]:
        return self.patterns['hashtag'].findall(text)

    def extract_currency(self, text: str) -> List[str]:
        return self.patterns['currency'].findall(text)

    def extract_all(self, text: str) -> Dict[str, List[str]]:
        """
        Extract all supported data types from text and return as a dictionary.
        """
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'credit_cards': self.extract_credit_cards(text),
            'times': self.extract_times(text),
            'html_tags': self.extract_html_tags(text),
            'hashtags': self.extract_hashtags(text),
            'currency': self.extract_currency(text)
        }

