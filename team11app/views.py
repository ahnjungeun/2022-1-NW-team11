from django.shortcuts import render,HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

nextId = 1
inputNum = [
]

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


@csrf_exempt
def create(request):

  global inputNum
  inputList = ''
  if inputNum != None:
    for userInput in inputNum:
      inputList += f'<li>{userInput["id"]} {userInput["answer"]}</li>'
  intro = f'''
      <p>입력한 숫자:</p>
      {inputList}
    '''

  answerNumber = 123

  global nextId
  if request.method == 'GET':
    article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="gameNum" placeholder="title"></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(intro+article))
  elif request.method == 'POST':
    gameNum = int(request.POST['gameNum'])
    newInputNum = {"id":nextId, "answer":gameNum}
    inputNum.append(newInputNum)
    if answerNumber == gameNum:
      return redirect('/')
    url = '/create/'
    nextId = nextId + 1
    return redirect(url)











# def show(request,answer): # url에서 show/answer로 들어온 값을 인자로
#   return HttpResponse('결과보여주기'+answer)
