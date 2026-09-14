from dotenv import load_dotenv
load_dotenv()

from langchain_google_gemini import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
que = "Whos is PM of India?"
result = llm.invoke(que)
print(result.content)