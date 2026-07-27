import re

# Sample text data (you can modify this)
text_data = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
prefix_example
suffix_test
"""

# Functions for each feature

def search_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    print("Dates Found:", re.findall(pattern, text))


def search_phone(text):
    pattern = r'\b[6-9]\d{9}\b'
    print("Phone Numbers Found:", re.findall(pattern, text))


def search_hashtag(text):
    pattern = r'#\w+'
    print("Hashtags Found:", re.findall(pattern, text))


def search_mention(text):
    pattern = r'@\w+'
    print("Mentions Found:", re.findall(pattern, text))


def search_prefix(text):
    prefix = input("Enter prefix: ")
    pattern = r'\b' + re.escape(prefix) + r'\w*'
    print("Prefix Matches:", re.findall(pattern, text))


def search_suffix(text):
    suffix = input("Enter suffix: ")
    pattern = r'\w*' + re.escape(suffix) + r'\b'
    print("Suffix Matches:", re.findall(pattern, text))


# Menu-driven program
def main():
    while True:
        print("\n--- Pattern Matching Engine ---")
        print("1. Search Date")
        print("2. Search Phone Number")
        print("3. Search Hashtag")
        print("4. Search Mention")
        print("5. Search Prefix")
        print("6. Search Suffix")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            search_date(text_data)
        elif choice == '2':
            search_phone(text_data)
        elif choice == '3':
            search_hashtag(text_data)
        elif choice == '4':
            search_mention(text_data)
        elif choice == '5':
            search_prefix(text_data)
        elif choice == '6':
            search_suffix(text_data)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()