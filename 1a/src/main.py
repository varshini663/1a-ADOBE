#!/usr/bin/env python3
import os
import json
import time
from pdf_processor import PDFOutlineExtractor

def main():
    print("PDF Outline Extractor starting...")
    start_time = time.time()
    
    # Create the extractor and process all PDFs
    extractor = PDFOutlineExtractor()
    extractor.process_pdfs()
    
    end_time = time.time()
    print(f"Processing completed in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()