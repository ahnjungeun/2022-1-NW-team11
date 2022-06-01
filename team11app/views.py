from django.shortcuts import render,HttpResponse

# Create your views here.

inputNum = [
  {'id':1,'answer':'뭐라고 하지'}
]

def HTMLTemplate():
  global inputNum
  inputList = ''
  for userInput in inputNum:
    inputList += f'<li>{userInput["id"]} {userInput["answer"]}</li>'
  # f빼먹지 말아라...abs(x)
  return f'''
    <html>
      <body>
        <h1>숫자야구</h1>
        <p>입력한 숫자:</p>
        <ul>
          {inputList}
        </ul>
      </body>
    </html>

  '''

def index(request): # '''긴 문자열 입력'''
  return HttpResponse(HTMLTemplate())

def input(request):
  return HttpResponse('숫자입력')

def show(request,answer): # url에서 show/answer로 들어온 값을 인자로
  return HttpResponse('결과보여주기'+answer)
