conversation_history=[]


def add_to_memory(

    question,

    answer

):

    conversation_history.append({

        "question":question,

        "answer":answer
    })


    MAX_HISTORY=5


    if len(
        conversation_history
    )>MAX_HISTORY:

        conversation_history.pop(
            0
        )


def get_memory():

    history_text=""


    for item in conversation_history:

        history_text += f"""

User:
{item['question']}

Assistant:
{item['answer']}

"""


    return history_text