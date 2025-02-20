# PDF Scraper with Automation

## 📌 Project Overview

This project automates the extraction of text from PDFs in a given directory and stores the extracted content for future use. The extracted text is saved in an SQLite database for structured storage, enabling efficient querying and retrieval.

## 🎯 Features

- Extracts text from PDFs efficiently.
- Processes all PDFs in a directory automatically.
- Stores extracted text in an SQLite database for structured access.
- Provides a CLI-based execution for ease of use.
- Ensures modular and scalable code architecture.
- Implements **logging** to track processing steps and errors.

## 🛠️ Why PyMuPDF?

This project utilizes **PyMuPDF** (also known as Fitz) over other PDF libraries like **PDFMiner** or **PyPDF2** due to:

- **Speed & Efficiency:** PyMuPDF is significantly faster in extracting text from PDFs.
- **Accuracy:** It retains the document structure better compared to other parsers.
- **Lightweight:** Consumes less memory and provides efficient text extraction.
- **Support for Complex PDFs:** Handles embedded fonts and complex document layouts effectively.

## 📄 Supported PDF Types

This tool is best suited for extracting text from:

- **Digitally Generated PDFs:** PDFs created directly from software like Microsoft Word, LaTeX, or InDesign.
- **Machine-Readable PDFs:** Documents where the text layer is selectable and extractable.

### ❌ Limitations

- **Scanned PDFs & Image-Based PDFs:** Lacks built-in OCR functionality; cannot extract text from scanned images without external OCR tools (e.g., Tesseract or Adobe OCR).
- **Encrypted or Restricted PDFs:** May not extract text from protected PDFs unless permissions allow it.
- **Poorly Formatted PDFs:** May struggle with extracting correctly structured text from heavily formatted PDFs with complex layouts.

## 📑 Logging System

The project includes a **logging system** to track operations in real-time and store them in `scraper.log`.

### 📌 Why Logging?

- ✅ Tracks each step of execution (PDF scanning, extraction, database storage).
- ✅ Records errors and warnings for debugging.
- ✅ Provides timestamps for process tracking.

### 📄 Logging Implementation

- **Log File**: All logs are stored in `scraper.log`.
- **Logging Levels**:
  - `INFO` → Tracks normal operations.
  - `WARNING` → Logs non-critical issues (e.g., duplicate PDFs).
  - `ERROR` → Captures failures (e.g., file read errors).

## 🤖 Why PDF Text Extraction is Important?

PDF text extraction is crucial for:

- **Data Mining & Research:** Extracting insights from large volumes of documents.
- **Automated Report Analysis:** Processing business reports, invoices, and financial statements.
- **Natural Language Processing (NLP):** Analyzing and processing text for sentiment analysis, keyword extraction, and entity recognition.
- **Searchable Document Archives:** Converting unstructured PDF content into structured databases for easy retrieval and indexing.

## 📂 Project Structure

```
📁 pdf_scraper
│── extractor.py       # Extracts text from PDFs
│── processor.py       # Scans directory and processes PDFs
│── database.py        # Handles SQLite database interactions
│── logger.py # Manages logging system
│── main.py            # CLI entry point for execution
│── requirements.txt   # Dependencies
│── README.md          # Project documentation
```

## 🚀 Installation & Usage

### 1️⃣ Setup Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 2️⃣ Run the Script

```sh
python main.py --directory /path/to/pdfs
```

### 3️⃣ Query Extracted Text (Example SQLite Query)

```sql
SELECT * FROM pdf_text WHERE filename = 'example.pdf';
```

---

This project provides a scalable and efficient solution for automated PDF text extraction and storage, enabling powerful document processing capabilities.
