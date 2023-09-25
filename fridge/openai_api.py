import os
import bardapi

#os.environ['_BARD_API_KEY'] = 'your API_KEY'


async def chat_bard(msg):
    response = bardapi.core.Bard().get_answer(msg)

    # 선택형 답변을 모두 보여주기
    # for i, choice in enumerate(response['choices']):
    #    print(f"Choice {i+1}:\n", choice['content'][0], "\n")

    return response['content']

