import argparse
import os
from pdf_scraper.processor import process_pdfs_in_directory


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract text from all PDFs in a directorty")
    parser.add_argument(
        "directory", help="Path to the directory containing PDFs")
    parser.add_argument("output", help="Output file to save extracted text")

    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print("Error: Directory does not exists!")
    else:
        process_pdfs_in_directory(args.directory, args.output)
