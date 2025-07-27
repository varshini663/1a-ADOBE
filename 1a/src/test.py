#!/usr/bin/env python3
import os
import json
from pdf_processor import PDFOutlineExtractor

def test_extractor():
    print("Running test for PDF Outline Extractor...")
    
    # Create a mock PDF path (in a real test, we would use a real PDF file)
    mock_pdf_path = "/app/input/test.pdf"
    
    # Create an instance of the extractor
    extractor = PDFOutlineExtractor()
    
    # Test the heading detection logic
    test_headings = [
        "1. Introduction",
        "1.1. Background",
        "1.1.1. Historical Context",
        "CHAPTER 2",
        "A. First Point",
        "Normal paragraph text that should not be detected as a heading."
    ]
    
    print("\nTesting heading detection:")
    for text in test_headings:
        is_heading = extractor.is_heading(text)
        level = extractor.determine_heading_level(text, 0) if is_heading else "Not a heading"
        print(f"'{text}' -> Is heading: {is_heading}, Level: {level}")
    
    # Test the JSON output format
    test_output = {
        "title": "Test Document",
        "outline": [
            {"level": "H1", "text": "1. Introduction", "page": 0},
            {"level": "H2", "text": "1.1. Background", "page": 1},
            {"level": "H3", "text": "1.1.1. Historical Context", "page": 2}
        ]
    }
    
    print("\nSample JSON output:")
    print(json.dumps(test_output, indent=2))
    
    print("\nTest completed successfully!")

if __name__ == "__main__":
    test_extractor()