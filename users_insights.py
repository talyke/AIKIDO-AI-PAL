from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)  # Stores past messages

def store_interaction(user_input, ai_response):
    """Save user interactions for future personalization."""
    memory.save_context({"input": user_input}, {"output": ai_response})

def retrieve_memory():
    """Fetch previous conversations to shape future responses."""
    past_chats = memory.load_memory_variables({})
    return past_chats if past_chats else "No conversation history yet."