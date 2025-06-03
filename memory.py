from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = "Let me think about that..."  # Placeholder for AI response
    memory.save_context({"input": user_input}, {"output": response})

    print("Aikido AI Buddy:", response)
    print("\nMemory:", memory.load_memory_variables({}))  # Shows stored chats