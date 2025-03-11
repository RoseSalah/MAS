def limit_history(history, max_entries=4):
    return history[-max_entries:]

def count_tokens(messages):
    return sum(len(m["content"].split()) for m in messages)
