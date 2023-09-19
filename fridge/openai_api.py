import openai
import os

openai.api_key = os.getenv('openai_API_KEY')
if openai.api_key is None:
    print("Not Available API_KEY")

class openai_bot:
    def __init__(self):
        with open("fridge/mode.txt", 'r') as f:
            self.sys_order = ' '.join(f.readlines())
            # 대화 내용을 저장할 리스트를 생성하고, 시스템 명령어를 첫번째 메시지로 추가
        self.messages = [{"role": "system", "content": self.sys_order}]
        # 토큰 갯수 초기화
        self.token_num = 0

    async def getquery(self, question):
        # 사용자의 질문을 메시지 리스트에 추가
        self.messages.append({"role": "user", "content": question})
        # openai API를 사용하여 GPT-3.5 모델로부터 답변 생성
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=self.messages)
        answer = completion['choices'][0]['message']['content']
        # 생성된 답변을 메시지 리스트에 추가
        self.messages.append({"role": "assistant", "content": answer})
        return answer

    def messages_clear(self):
        # 대화 내용을 저장할 리스트를 생성하고, 시스템 명령어를 첫번째 메시지로 추가
        self.messages = [{"role": "system", "content": self.sys_order}]
