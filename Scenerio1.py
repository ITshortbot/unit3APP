import csv
import re
import sys
from pathlib import Path


def read_books(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))


def display_all_books(books):
    print("\nALL BOOK RECORDS")
    print("-" * 90)
    if not books:
        print("No books found.")
        return

    for book in books:
        print(
            f"Title: {book.get('Title', '')} | "
            f"Author: {book.get('Author', '')} | "
            f"ISBN: {book.get('ISBN', '')} | "
            f"Category: {book.get('Category', '')} | "
            f"Price: ₹{book.get('Price', '')}"
        )
    print("-" * 90)


def search_books_by_title_keyword(books, keyword):
    pattern = re.compile(rf"^{re.escape(keyword)}", re.IGNORECASE)
    return [book for book in books if pattern.match(str(book.get('Title', '')))]


def main():
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
    else:
        file_path = Path(__file__).with_name("books.csv")

    books = read_books(file_path)
    display_all_books(books)

    keyword = input("\nEnter the title keyword to search: ").strip()
    matches = search_books_by_title_keyword(books, keyword)

    print(f"\nMatching books whose title starts with '{keyword}':")
    if not matches:
        print("No matching records found.")
        return

    for book in matches:
        print(
            f"Title: {book.get('Title', '')} | "
            f"Author: {book.get('Author', '')} | "
            f"ISBN: {book.get('ISBN', '')} | "
            f"Category: {book.get('Category', '')} | "
            f"Price: ₹{book.get('Price', '')}"
        )


if __name__ == "__main__":
    main()
