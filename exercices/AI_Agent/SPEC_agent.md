# Technical Document QA Agent - Functional Specification

## 1. Project Objective

Develop a RAG (Retrieval-Augmented Generation) agent capable of answering technical questions from a collection of:

- Markdown documents (`.md`)
- HTML documents (`.html`)
- Datasheets
- Scientific papers
- Technical documentation

The agent must answer **only using the content available in the provided documents**.

If the answer cannot be found in the indexed documents, the agent must return:

```text
I could not find the information in the provided documents.
```

The agent must minimize hallucinations and always provide sources.

---

# 2. Functional Requirements

## Inputs

### Documents

The agent must support:

```text
*.md
*.html
```

Examples:

```text
docs/
├── k230_datasheet.md
├── zephyr_semaphores.html
├── research_paper.html
```

### User Question

Example:

```text
What AI frameworks are supported by the K230?
```

---

## Outputs

### Success Case

```text
Answer:

The K230 supports the following AI frameworks:

- TensorFlow
- PyTorch
- TFLite
- PaddlePaddle
- ONNX

Sources:
- k230_datasheet.md / KPU subsystem
```

### No Information Found

```text
Answer:

I could not find the information in the provided documents.
```

---

# 3. High-Level Architecture

```text
Documents MD / HTML
           ↓
      Document Loader
           ↓
          Parser
           ↓
        Chunking
           ↓
       Embeddings
           ↓
       ChromaDB
           ↓
        Retriever
           ↓
       Mistral API
           ↓
      Answer Builder
           ↓
   Answer + Citations
```

---

# 4. Phase 1 - Document Loading

## Objective

Automatically load all markdown and HTML files located in a target directory.

## Input

```text
docs/
```

## Tasks

- Scan directory recursively
- Detect supported file formats
- Load content into memory

## Output Structure

```python
{
    "source": "k230_datasheet.md",
    "content": "document text"
}
```

---

# 5. Phase 2 - Parsing

## Objective

Extract clean textual content.

## Markdown Parsing

Keep:

```text
Titles
Subtitles
Paragraphs
Lists
Tables
```

Remove:

```text
Images
Unused links
Markdown formatting artifacts
```

---

## HTML Parsing

Extract:

```text
h1
h2
h3
h4

p

table

li
```

Remove:

```text
script
style
navigation menus
footer
advertisements
```

---

## Output

```python
{
    "source": "k230_datasheet.md",
    "content": "clean parsed text"
}
```

---

# 6. Phase 3 - Chunking

## Objective

Split documents into smaller semantic units.

---

## Recommended Strategy

### Header-Aware Chunking

Use document structure whenever available.

Example:

```markdown
# CPU

content...

# Memory

content...

# Security

content...
```

Each section becomes one or several chunks.

---

## Parameters

```text
Chunk Size = 1000 characters

Chunk Overlap = 150 characters
```

---

## Chunk Metadata

```python
{
    "content": "...",
    "source": "k230_datasheet.md",
    "section": "Memory"
}
```

---

## Desired Properties

Chunks must:

- Be self-contained
- Keep context
- Preserve section titles
- Preserve metadata

---

# 7. Phase 4 - Embeddings

## Objective

Convert chunks into vectors.

---

## Embedding Model

Use Mistral embedding model.

Example:

```text
mistral-embed
```

---

## Workflow

```text
Chunk
   ↓
Embedding Model
   ↓
Vector
```

---

## Output Example

```python
{
    "embedding": [...],
    "content": "...",
    "source": "...",
    "section": "..."
}
```

---

# 8. Phase 5 - Vector Database

## Technology

Use:

```text
ChromaDB
```

---

## Stored Data

For every chunk:

```text
Embedding
Chunk Content
Source File
Section
```

---

## Example

```python
{
  "source":"k230_datasheet.md",
  "section":"KPU subsystem"
}
```

---

# 9. Phase 6 - Retrieval

## Objective

Find the most relevant chunks for a user question.

---

## Input

```text
What AI frameworks are supported by the K230?
```

---

## Retrieval Pipeline

```text
Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Top K Chunks
```

---

## Parameters

```text
top_k = 5
```

---

## Example Output

```python
[
    chunk_12,
    chunk_37,
    chunk_42,
    chunk_55,
    chunk_58
]
```

---

# 10. Phase 7 - Retrieval Validation

## Objective

Reduce hallucinations.

---

## Similarity Score Check

Each retrieved chunk has a similarity score.

Example threshold:

```text
0.50
```

---

## Logic

### Score Above Threshold

```text
Proceed to LLM
```

### Score Below Threshold

```text
Skip LLM call
```

Return:

```text
I could not find the information in the provided documents.
```

---

# 11. Phase 8 - Answer Generation using Mistral

## LLM

Use:

```text
mistral-large
```

or

```text
mistral-medium
```

---

## System Prompt

```text
You are a technical assistant.

Use ONLY the provided context.

Do not use external knowledge.

If the answer cannot be found in the provided context, answer exactly:

"I could not find the information in the provided documents."

Always cite the source documents and sections used for the answer.
```

---

## User Prompt

```text
Context:

{retrieved_chunks}

Question:

{user_question}
```

---

## Expected Behavior

The model must:

- Use only retrieved information
- Avoid hallucinations
- Summarize technical information
- Cite document sources

---

# 12. Phase 9 - Source Attribution

## Objective

Provide traceability.

---

## Example Output

```text
Sources:

- k230_datasheet.md / KPU subsystem
- k230_datasheet.md / CPU subsystem
```

---

# 13. Final Answer Format

## Positive Match

```text
Answer:

The K230 supports:

- TensorFlow
- PyTorch
- TFLite
- PaddlePaddle
- ONNX

Sources:

- k230_datasheet.md / KPU subsystem
```

---

## No Match

```text
Answer:

I could not find the information in the provided documents.
```

---

# 14. Optional V2 Features

## Hybrid Search

Combine:

```text
Vector Search
+
BM25 Search
```

To improve retrieval quality.

---

## Re-ranking

Add a reranker after retrieval:

```text
Retriever
     ↓
Reranker
     ↓
Top Chunks
```

---

## Arize Phoenix Integration

Monitor:

```text
Question
↓
Retrieved Chunks
↓
Prompt
↓
LLM Response
↓
Sources
```

Useful for:

- Retrieval debugging
- Chunking comparison
- Hallucination analysis

---

# 15. Recommended Technology Stack

## Backend

```text
Python
```

---

## Document Processing

```text
BeautifulSoup
Markdown Parser
```

---

## RAG

```text
LangChain
```

---

## Embeddings

```text
Mistral Embeddings
```

---

## Vector Database

```text
ChromaDB
```

---

## LLM

```text
Mistral Large
```

---

## Monitoring

```text
Arize Phoenix
```

(Optional)

---

## Frontend

```text
Streamlit
```

(Optional)

---

# 16. MVP Development Order

Implement in this exact sequence:

```text
1. Document Loader
2. Parser
3. Chunking
4. Mistral Embeddings
5. ChromaDB
6. Retrieval
7. Mistral LLM
8. Source Attribution
9. Similarity Threshold Validation
10. Simple UI
```

This delivers a complete and production-ready first version of the Technical Document QA Agent.