import io
from typing import Optional

def parse_pdf(file_bytes: bytes) -> str:
    """Extract text from PDF file bytes using PyMuPDF."""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except ImportError:
        return _parse_pdf_fallback(file_bytes)
    except Exception as e:
        return f"Error parsing PDF: {str(e)}"


def _parse_pdf_fallback(file_bytes: bytes) -> str:
    """Fallback PDF parser using pypdf if PyMuPDF not available."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(file_bytes))
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        return f"Could not parse PDF: {str(e)}"


def parse_docx(file_bytes: bytes) -> str:
    """Extract text from DOCX file bytes using python-docx."""
    try:
        import docx
        doc = docx.Document(io.BytesIO(file_bytes))
        paragraphs = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(paragraphs)
    except Exception as e:
        return f"Error parsing DOCX: {str(e)}"


def parse_resume(uploaded_file) -> Optional[str]:
    """
    Main entry point — detects file type and parses accordingly.
    Returns extracted text or None on failure.
    """
    if uploaded_file is None:
        return None

    file_bytes = uploaded_file.read()
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return parse_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return parse_docx(file_bytes)
    else:
        return "Unsupported file type. Please upload PDF or DOCX."
