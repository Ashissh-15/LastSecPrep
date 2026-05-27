import os

from google import genai
from dotenv import load_dotenv

from memory.chat_memory import (
    get_memory
)


load_dotenv()


client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)


def generate_response(
    query,
    retrieved_chunks,
    source_info
):

    # ====================
    # Retrieved context
    # ====================

    context = "\n\n".join(
        retrieved_chunks
    )


    # ====================
    # Previous chat memory
    # ====================

    chat_history = get_memory()


    prompt = f"""
You are an academic study assistant.

Rules:

1. Answer ONLY from provided context
2. Use previous conversation only for continuity
3. Do NOT invent facts
4. If information is missing say exactly:
"I could not find this in the uploaded materials."
5. Explain concepts clearly for students
6. Use headings and bullet points where useful
7. Do not mention internal system details

Previous Conversation:

{chat_history}


Retrieved Context:

{context}


Question:

{query}


Answer:
"""


    try:

        response = (
            client.models.generate_content(

                model="gemini-2.0-flash",

                contents=prompt
            )
        )

        answer = response.text


    except Exception as e:

        print(
            f"\nGemini API failed: {e}"
        )


        answer = """
Gemini API unavailable or quota exceeded.

Retrieved information:

""" + "\n".join(
            retrieved_chunks[:2]
        )


    # ====================
    # Add citations
    # ====================

    citations = []

    seen = set()


    for source in source_info:

        key = (
            source["source"],
            source["page"]
        )


        if key not in seen:

            seen.add(
                key
            )

            citations.append(

                f"- {os.path.basename(source['source'])} "
                f"(Page: {source['page']})"

            )


    if citations:

        answer += "\n\nSources:\n"

        answer += "\n".join(
            citations
        )


    return answer