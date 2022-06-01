from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.

nextId = 1
inputNum = []

def HTMLTemplate(content):
  return f'''
    <html>
      <body>
        <h1><a href="/">숫자야구</a></h1>
        {content}
      </body>
    </html>
  '''

def index(request): # '''긴 문자열 입력'''
  global inputNum
  inputNum = []
  start = '<a href="/create/">시작하기</a>'
  return HttpResponse(HTMLTemplate(start))

def showList():
  global inputNum
  inputList = ''
  if inputNum != None:
    for userInput in inputNum:
      inputList += f'<li>{userInput["id"]}번째 {userInput["answer"]} {userInput["desc"]}</li>'
  intro = f'''
      <p>입력한 숫자:</p>
      {inputList}
    '''
  return intro
  
@csrf_exempt
def create(request):

  intro = showList()
  # answerNumber = random.randint(100, 999)
  answerNumber = 123

  global nextId, inputNum
  if request.method == 'GET':
    article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="userNum" placeholder="title"></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(intro+article))
  elif request.method == 'POST':
    userNum = int(request.POST['userNum'])
    newInputNum = {"id":nextId, "answer":userNum, "desc":YaguGame(answerNumber,userNum)}
    inputNum.append(newInputNum)
    
    if "3s" == YaguGame(answerNumber,userNum):
    # if answerNumber == userNum:
      article = '''
        <p>정답입니다.</p>
        <a href="/create">다시 시작하기</a>
      '''
      intro = showList()
      inputNum = []
      nextId = 1
      return HttpResponse(HTMLTemplate(intro+article))
    nextId = nextId + 1
    url = '/create/'
    return redirect(url)

# 여기 수정해주세요.
def YaguGame(answerNum,userNum):
  if answerNum == userNum:
    resultStr = "3s"
  else:
    resultStr = "정답 아님"
  return resultStr










# def show(request,answer): # url에서 show/answer로 들어온 값을 인자로
#   return HttpResponse('결과보여주기'+answer)
