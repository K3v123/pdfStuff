# pdfStuff - PDF Utilities Toolkit

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A collection of small Python scripts for PDF compression, merging, and basic image conversion. Designed for handling sensitive documents with minimal dependencies.

## ⚠️ Critical Disclaimer
**I AM NOT ACCOUNTABLE FOR ANY DATA LOSS, PRIVACY BREACHES, OR DAMAGES RESULTING FROM THE USE OF THESE TOOLS.**  
These scripts are provided "as-is" without warranties. Always:
1. Verify output files before discarding originals
2. Handle sensitive documents in isolated environments
3. Comply with your organization's data handling policies

## Tools Included

### 1. PDF Compressor (`compressPdf.py`)
- Compresses text/vector content using `pypdf`
- **Limitation**: Minimal reduction for image-heavy PDFs
- Features:
  - Size comparison report
  - Metadata preservation
  - Background processing

### 2. PDF Merger (`pdf merge.py`)
- Combines two PDF files sequentially


### 3. Basic Image Converter (`imgTopdf.py`)
