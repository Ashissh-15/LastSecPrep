# LastSecPrep – Multimodal RAG-based Academic Study Assistant

LastSecPrep is a **multimodal Retrieval-Augmented Generation (RAG) system** designed to simplify exam preparation by converting scattered academic materials into an interactive study assistant. Instead of manually searching through large PDFs, PowerPoints, and Word documents, users simply provide a folder containing study resources and ask questions naturally.

The system processes study materials, extracts text, tables, and educational images/diagrams, stores semantic representations in a vector database, and generates grounded responses using an LLM.

---

## Features

* Supports multiple document types:

  * PDF
  * DOCX
  * PPT/PPTX

* Multimodal document understanding:

  * Text extraction
  * Table extraction
  * Educational image/diagram processing
  * OCR-based image text extraction

* Semantic search pipeline:

  * Embedding generation
  * ChromaDB vector storage
  * Semantic retrieval
  * Reranking for improved relevance

* Conversational capabilities:

  * Multi-turn chat memory
  * Context-aware follow-up questions
  * Source citations for responses

* Grounded response generation:

  * Gemini API / Local LLM support (Ollama)

---

## System Architecture

```text
Study Material Folder
        ↓
Document Loaders
(PDF / DOCX / PPT)
        ↓
Text + Table + Image Extraction
        ↓
Semantic Chunking
        ↓
Embedding Generation
        ↓
ChromaDB Vector Store
        ↓
Retrieval + Reranking
        ↓
LLM (Gemini / Ollama)
        ↓
Grounded Answer + Citations
```

---

## Tech Stack

### Languages

* Python

### Vector Database

* ChromaDB

### LLM

* Gemini API
* Ollama (local model support)

### NLP / Retrieval

* Sentence Transformers
* Custom Semantic Chunking
* Reranking

### Document Processing

* PyMuPDF
* python-docx
* python-pptx

### OCR & Image Processing

* Tesseract OCR
* Pillow

---

## Project Structure

```text
LastSecPrep/
│
├── loaders/
│   ├── pdf_loader.py
│   ├── docx_loader.py
│   ├── ppt_loader.py
│   └── image_extractor.py
│
├── chunking/
│   └── text_chunker.py
│
├── embeddings/
│   └── embedding_model.py
│
├── vector_db/
│   └── chroma_store.py
│
├── retrieval/
│   ├── retriever.py
│   └── reranker.py
│
├── llm/
│   └── gemini_handler.py
│
├── memory/
│   └── chat_memory.py
│
├── data/
│
├── chroma_db/
│
├── main.py
│
└── requirements.txt
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/LastSecPrep.git

cd LastSecPrep
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Project

Place study materials inside:

```text
data/
```

Run:

```bash
python main.py
```

Example:

```text
Ask your question:

What are the stages of STLC?

Explain the white box testing image

Give me the black box vs white box comparison table
```

---

## Future Improvements

* Streamlit web interface
* Incremental indexing
* Handwritten note understanding

---

## Motivation

Students often collect large amounts of study material before exams and spend significant time searching for specific concepts. LastSecPrep aims to reduce this effort by transforming static resources into an intelligent, searchable study assistant.
