import os
import time

AGENT_NAME = "MyAgent"
DEFAULT_ANSWER = "I'm sorry, I don't have an answer for that."


class Agent:
    def __init__(self):
        self.name = AGENT_NAME
        self.files = []

    def upload_file(self, file_path):
        if os.path.isfile(file_path):
            self.files.append(file_path)
            print("File uploaded successfully.")
        else:
            print("File not found. Please provide a valid file path.")

    def generate_answer(self, question):
        answer = self.search_files(question)
        if answer:
            return answer
        else:
            return self.generate_default_answer(question)

    def search_files(self, question):
        for file_path in self.files:
            with open(file_path, 'r') as file:
                content = file.read()
                if question in content:
                    return content
        return None

    def generate_default_answer(self, question):
        return DEFAULT_ANSWER


# Creating the agent
agent = Agent()

# User interaction loop
while True:
    user_input = input("User: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    elif user_input.lower() == "upload":
        file_path = input("Enter file path: ")
        agent.upload_file(file_path)

    else:
        answer = agent.generate_answer(user_input)
        print(f"{AGENT_NAME}: {answer}")

    time.sleep(0.5)  # Sleep to simulate processing time
