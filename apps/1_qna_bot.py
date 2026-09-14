from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")


def response_text(content):
    if isinstance(content, str):
        return content
    return "".join(
        part.get("text", "") for part in content if isinstance(part, dict)
    )

# while True:
#     query = input("user: ")
#     if query.lower() in ["quit", "exit", "bye"]:
#         print("GoodBye")
#         break
#     res = llm.invoke(query)
#     print(res.content)

st.title("Ask Buddy AI QnA Bot")
st.markdown("My QnA Bot with langchain and Google Gemini 3.6")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)




query = st.chat_input("Ask me anything")
if query:
    st.session_state.messages.append({"role":"user", "content":query}) 
    st.chat_message("user").markdown(query)
    
    res  = llm.invoke(query)
    answer = response_text(res.content)
    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
    


