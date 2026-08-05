import re

# -----------------------------
# Sample Product Database
# -----------------------------
products = [
    "Apple iPhone 14",
    "Apple MacBook Air",
    "Samsung Galaxy S23",
    "Dell Inspiron Laptop",
    "HP Pavilion Laptop",
    "Sony Wireless Headphones",
    "Apple AirPods Pro",
    "Samsung Smart TV",
    "Lenovo ThinkPad Laptop",
    "Asus Gaming Laptop"
]

# -----------------------------
# Search Functions
# -----------------------------

def exact_search(keyword):
    pattern = rf'^{re.escape(keyword)}$'
    return [p for p in products if re.search(pattern, p, re.IGNORECASE)]

def prefix_search(keyword):
    pattern = rf'^{re.escape(keyword)}'
    return [p for p in products if re.search(pattern, p, re.IGNORECASE)]

def suffix_search(keyword):
    pattern = rf'{re.escape(keyword)}$'
    return [p for p in products if re.search(pattern, p, re.IGNORECASE)]

def partial_search(keyword):
    pattern = rf'{re.escape(keyword)}'
    return [p for p in products if re.search(pattern, p, re.IGNORECASE)]

# -----------------------------
# Display Results
# -----------------------------

def display_results(results, search_type):
    print(f"\n--- {search_type} Results ---")
    if results:
        for product in results:
            print(product)
    else:
        print("No matching products found.")
    
    print(f"Total Matches: {len(results)}")

# -----------------------------
# Main Program
# -----------------------------

def main():
    keyword = input("Enter search keyword: ")

    # Perform searches
    exact = exact_search(keyword)
    prefix = prefix_search(keyword)
    suffix = suffix_search(keyword)
    partial = partial_search(keyword)

    # Display results
    display_results(exact, "Exact Search")
    display_results(prefix, "Prefix Search")
    display_results(suffix, "Suffix Search")
    display_results(partial, "Partial Search")

# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    main()