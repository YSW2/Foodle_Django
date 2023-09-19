import requests

def getname(code):

    url = 'https://gs1.koreannet.or.kr/pr/' + code
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text

    else:
        print("HTTP 요청이 실패했습니다.")
        html_content = None

    return html_content