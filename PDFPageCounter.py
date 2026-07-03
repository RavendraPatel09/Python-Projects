from PyPDF2 import PdfReader

def get_pdf_info(path):
    reader = PdfReader(path)
    info = {
        "pages": len(reader.pages),
        "encrypted": reader.is_encrypted
    }
    if reader.metadata:
        info["title"] = reader.metadata.title or "Unknown"
        info["author"] = reader.metadata.author or "Unknown"
    return info

def main():
    path = input("PDF file path: ")
    info = get_pdf_info(path)
    print(f"Pages: {info['pages']}")
    print(f"Encrypted: {info['encrypted']}")
    print(f"Title: {info.get('title', 'Unknown')}")
    print(f"Author: {info.get('author', 'Unknown')}")

if __name__ == "__main__":
    main()
