import os

from loaders.file_router import load_file
from chunking.text_chunker import chunk_documents
from memory.chat_memory import add_to_memory
from vector_db.chroma_store import store_documents


# ==========================
# CONFIG
# ==========================

DATA_FOLDER = "data"

# Set True only when:
# - new files added
# - chunking changes
# - OCR/tables added
# - ingestion changes

REBUILD_DB = True


# ==========================
# DATABASE REBUILD
# ==========================

if REBUILD_DB:

    all_documents = []

    for root, dirs, files in os.walk(DATA_FOLDER):

        for file in files:

            # Skip temporary Office files
            if file.startswith("~$"):
                continue

            file_path = os.path.join(
                root,
                file
            )

            print(
                f"Processing: {file_path}"
            )

            try:

                documents = load_file(
                    file_path
                )

                all_documents.extend(
                    documents
                )

            except Exception as e:

                print(
                    f"Failed: {file_path}"
                )

                print(
                    f"Error: {e}"
                )


    print("\nTOTAL RAW DOCUMENTS:")
    print(len(all_documents))


    chunked_documents = chunk_documents(
        all_documents
    )


    print("\nTOTAL CHUNKS CREATED:")
    print(len(chunked_documents))


    print(
        "\nSTORING IN CHROMADB...\n"
    )


    store_documents(
        chunked_documents
    )


    print("\nDONE!")


    print(
        "\nSAMPLE CHUNKS:"
    )

    for i, chunk in enumerate(
        chunked_documents[:3]
    ):

        print("\n----------------")

        print(
            f"Chunk {i+1}"
        )

        print(
            chunk["text"]
        )


# ==========================
# IMPORT AFTER DB BUILD
# ==========================

from retrieval.retriever import retrieve_relevant_chunks
from llm.gemini_handler import generate_response


# ==========================
# QUERY LOOP
# ==========================

while True:

    query = input(
        "\nAsk your question (exit to quit): "
    )

    if query.lower() == "exit":
        break


    results = retrieve_relevant_chunks(
        query
    )


    if not results:

        print(
            "\nNo relevant information found."
        )

        continue


    retrieved_docs=[]

    source_info=[]


    for score,doc,metadata in results:

        retrieved_docs.append(doc)

        source_info.append({

            "source":metadata["source"],

            "page":metadata["page"]
        })


    answer=generate_response(
        query,
        retrieved_docs,
        source_info
    )


    print("\nANSWER:")
    print("-"*50)

    print(answer)

    add_to_memory(

        query,

        answer

    )