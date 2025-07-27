# PDF Outline Extractor

This project extracts structured outlines from PDF documents, identifying the title and headings (H1, H2, H3) with their corresponding page numbers.

## Approach

The PDF Outline Extractor uses a combination of techniques to identify document structure:

1. **Title Extraction**:
   - First attempts to extract from PDF metadata
   - Falls back to using the first line of the first page if metadata is unavailable

2. **Heading Detection**:
   - Uses multiple heuristics to identify headings:
     - Text formatting (capitalization, title case)
     - Numerical patterns (1., 1.1., etc.)
     - Roman numerals and alphabetic markers
     - Text length and position

3. **Heading Level Classification**:
   - Determines heading levels (H1, H2, H3) based on:
     - Numerical hierarchy in headings
     - Position in document
     - Text formatting characteristics
   - Ensures at least one heading of each required level

## Libraries Used

- **PyPDF2**: For PDF parsing and text extraction
- **Standard Python Libraries**: os, json, time, re

## How to Build and Run

### Prerequisites

- Docker installed on your system

### Building the Docker Image

```bash
docker build --platform linux/amd64 -t pdf-outline-extractor .
```

### Running the Solution

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output pdf-outline-extractor
```

On Windows PowerShell:

```powershell
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output pdf-outline-extractor
```

## Input and Output

### Input

Place PDF files in the `input` directory. The solution accepts PDFs up to 50 pages.

### Output

For each input PDF file, a corresponding JSON file will be generated in the `output` directory with the following format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## Performance

The solution is optimized to process a 50-page PDF in under 10 seconds, meeting the competition requirements.

## Limitations

- The heading detection relies on heuristics and may not perfectly identify all headings in documents with unusual formatting
- The solution works best with well-structured documents that use consistent formatting for headings