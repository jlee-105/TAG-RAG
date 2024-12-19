# from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage

# Ollama 모델 초기화
ollama = ChatOllama(base_url="http://localhost:11434", model="llama3.2")

# 테스트 프롬프트
test_prompt = "Hi"

message = HumanMessage(content=test_prompt)
print("message---------", message)

# message = "Hi"
# response = ollama(message)
# Ollama 호출
response = ollama.invoke([HumanMessage(content=test_prompt)])

# 결과 출력
#print("Ollama response:", response['content'])
print("llm_response: ", response.content)