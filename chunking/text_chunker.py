from nltk.tokenize import sent_tokenize
from utils.text_cleaner import clean_text


def chunk_documents(documents):

    chunked_documents=[]

    CHILD_SIZE=600
    OVERLAP=2


    for doc in documents:

        text=clean_text(doc["text"])

        sentences=sent_tokenize(text)

        parent_text=text

        current=[]
        current_len=0

        chunk_id=0


        for sentence in sentences:

            if current_len+len(sentence)>CHILD_SIZE:

                child_chunk=" ".join(current)

                if len(child_chunk)>100:

                    chunked_documents.append({

                        "text":child_chunk,

                        "parent_text":parent_text,

                        "source":doc["source"],

                        "page":doc["page"],

                        "chunk_id":chunk_id
                    })

                    chunk_id+=1


                overlap=current[-OVERLAP:]

                current=overlap
                current_len=sum(len(x) for x in overlap)


            current.append(sentence)
            current_len+=len(sentence)


        if current:

            child_chunk=" ".join(current)

            if len(child_chunk)>100:

                chunked_documents.append({

                    "text":child_chunk,

                    "parent_text":parent_text,

                    "source":doc["source"],

                    "page":doc["page"],

                    "chunk_id":chunk_id
                })


    return chunked_documents