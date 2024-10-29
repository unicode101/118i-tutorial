# The code was developed based on OpenAI File Search API. The code is further revised with the help of GitHub Copilot
#pip install --upgrade openai
import streamlit as st
import openai
import os
from openai import OpenAI, AssistantEventHandler

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Create the assistant
assistant = client.beta.assistants.create(
    name="Financial Analyst Assistant",
    instructions="You are an expert financial analyst. Use your knowledge base to answer questions about audited financial statements.",
    model="gpt-4o",
    tools=[{"type": "file_search"}],  # Use 'file_search' tool type
)

# Create a vector store called "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")

# Ready the files for upload to OpenAI
file_paths = ["pages/files/statement1.pdf", "pages/files/statement2.txt"]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

# Upload the user provided file to OpenAI
message_file = client.files.create(
    file=open("pages/files/statement1.pdf", "rb"), purpose="assistants"
)

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


# Display chat history
# Streamlit UI
st.title("Financial Analyst Assistant Chat Interface")

# Display chat history
for message in st.session_state.chat_history:
    role, content = message.split(" > ", 1)
    if role == "user":
        st.write(f"**User:** {content}")
    else:
        st.write(f"**Assistant:** {content}")

# User input
user_input = st.text_input("Ask a question about the financial statements:")

# Send message to assistant
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append(f"user > {user_input}")
        thread = client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        )

        class EventHandler(AssistantEventHandler):
            def on_text_created(self, text) -> None:
                st.session_state.chat_history.append(f"assistant > {text}")

            def on_tool_call_created(self, tool_call):
                pass  # No file search tool used here

            def on_message_done(self, message) -> None:
                # print a citation to the file searched (not applicable)
                st.text(message.content[0].text.value)  # Only display response

        # Then, we use the stream SDK helper
        # with the EventHandler class to create the Run
        # and stream the response.
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant.id,  # Assuming the assistant already exists
            instructions="Please address the user as Jane Smith. The user has a premium account.",
            event_handler=EventHandler(),
        ) as stream:
            stream.until_done()
