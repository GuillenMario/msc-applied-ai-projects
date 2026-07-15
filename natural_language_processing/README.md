# Natural Language Processing – MSc Applied AI

**Status:** This project is currently in its draft phase. The structure, workflow, and notebook are in place and reviewable, but some sections (metrics, results) may still be refined.

This section is a standalone project developed during my **Master's in Applied Artificial Intelligence**, focusing on building an **LLM + RAG (Retrieval-Augmented Generation) chatbot over tabular/document information** using ChromaDB, Sentence Transformers, and Hugging Face Transformers.

The project simulates an **end-to-end LLM + RAG pipeline**:
1. Reading and chunking source documents (PDFs).
2. Building a vector space of embedded chunks with ChromaDB.
3. Retrieving the most relevant chunks for a given query.
4. Generating grounded answers with a multilingual LLM.
5. Saving the final model and tokenizer for reuse.

---

## 📂 Folder Structure

```
natural_language_processing/
└── 01_LLM_RAG_Chatbot/
    └── chatbot_LLM_RAG.ipynb
```

---

## 📊 Notebook Overview

| # | Notebook | Description | Key Techniques | Results / Metrics |
|---|----------|-------------|----------------|------------------|
| 1 | [LLM + RAG Chatbot](01_LLM_RAG_Chatbot/chatbot_LLM_RAG.ipynb) | End-to-end RAG chatbot over document collections | ChromaDB vector store, `intfloat/multilingual-e5-large` embeddings, `Qwen/Qwen2.5-3B-Instruct` LLM, chunking with overlap | Qualitative Q&A evaluation over sample documents |

---

## 📊 Dataset

The source documents are not included due to size/licensing.

- Place your own PDF documents inside a `Documentos/` folder at the notebook's working directory (`BASE_DIR`).
- The notebook automatically creates the required working directories (`chroma/`, `checkpoints/`, `modelo_final_rag/`) if they do not exist.

---

## ⚙️ Environment Setup

The project runs on the same root environment as the rest of the repo. From repo root:

```bash
conda env create -f ../../environment.yml
conda activate applied_ai
```

Additional notes:
- A local **dedicated GPU (CUDA)** is recommended; the notebook automatically detects and reports GPU availability.
- A **Hugging Face account/token** is required to log in and access gated/limited models.
- Key libraries used: `torch`, `transformers`, `peft`, `sentence-transformers`, `chromadb`, `pypdf`.

---

## 📌 Key Takeaways

- Built a **RAG pipeline** using ChromaDB to store and retrieve embedded document chunks.
- Used a **multilingual embedding model** (`multilingual-e5-large`) and a **multilingual LLM** (`Qwen2.5-3B-Instruct`) to support cross-language queries (e.g., asking in Spanish about English documents).
- Learned that **chunk size and overlap** have a major impact on answer quality — larger chunks with more overlap were needed for the model to have enough context for complex questions.
- Found that **quantization and fine-tuning were not beneficial** for this use case, likely due to the small size of the dataset used, with both techniques underperforming the base model.

---

### **Final Thoughts**

Implementing the chatbot using the RAG technique with ChromaDB turned out to be relatively simple and easy to follow. This technique is especially useful for organizations that store large volumes of information in documents, such as regulations, product manuals, procedures, or internal documentation, since it allows that information to be queried efficiently using natural language.

However, to achieve satisfactory performance, it was necessary to adjust several system parameters:

- The chunk size and the overlap between chunks were increased considerably, since with smaller values the model rarely had enough context to correctly answer complex questions.
- Larger language and embedding models with multilingual support were selected. This made it possible to make queries in Spanish even when the documents were in English.
- Quantization and fine-tuning were not necessary for this implementation. In the tests performed, both techniques produced lower performance than the base model, which is probably due to the small size of the dataset used.
