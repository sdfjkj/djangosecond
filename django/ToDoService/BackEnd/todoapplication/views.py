# 클래스형 Views를 만들기 위해서 import
from django.views import View
# csrf 설정을 이한 import
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# 데이터 모델을 가져오기 위한 import
from .models import Todo

#날짜와 시간을 사용하기 위한 import
from datetime import datetime

# json으로 응답하기 위한 import
from django.http import JsonResponse

# 클라이언트의 정보를 json 문자열로 만들기 위한 import
import json

# Todo 클래스의 인스턴스를 딕셔너리로 변환해주는 함수
# JsonResponse로 JSON 데이터를 출력하고자 하면 빠르게 JSON문자열로 만들 때 dict만 가능
#dict는 JSON 문자열과 표현 방법이 같기 때문입니다.
# python application 개발자가 될거라면 함수를 만들 때 매개변수의 자료형을 기재하고 
# return type을 기재하는 형태로 만들어주는 것이 좋다
def todoToDictionary(todo:Todo) -> dict:
  result = {
    "id" :todo.id,
    "userid" : todo.userid,
    "title" : todo.title, 
    "done" : todo.done,
    "regdate" : todo.regdate,
    "moddate": todo.moddate
  }

# csrf  설정으로 클라이언트 애플리케이션을 별도로 구현하는 경우 필수
@method_decorator(csrf_exempt, name = 'dispatch')
class TodoView(View):
  def post(self, request):
    # 클라이언트의 데이터를 json형태로 가져오기
    request = json.loads(request.body)

    #userid와 title  매개변수 값을 읽어서 저장
    # 클라이언트에서 입력해주는 데이터만 읽어오면 된다
    userid = request["userid"]
    title = request["title"]

    # 모델 인스턴스 생성
    todo  = Todo()
    todo.userid = userid
    todo.title = title

    todo.save()
    # userid와 일치하는 데이터만 추출
    todos = Todo.objects.filter(userid=userid)

    # 결과 return
    return JsonResponse({"list":list(todos.values())})
  
  def get(self, request):
    #GET 방식에서 userid라는 파라미터를 읽기
    # userid = request.GET["userid"]
    # todos = Todo.objects.filter(userid = userid)
    userid = request.GET["userid"]
    todos = Todo.objects.filter()
    return JsonResponse({"list": list(todos.values())})

  def put(self, request):
    # 클라이언트의 데이터를 json형태로 가져오기
    request = json.loads(request.body)

    #userid와 id, done  매개변수 값을 읽어서 저장
    # 클라이언트에서 입력해주는 데이터만 읽어오면 된다
    userid = request["userid"]
    id = request["id"]
    done = request["done"]

    # 삽입 : 모델 인스턴스 생성
    # 수정 : 값을 찾아온다
    todo  = Todo.objects.get(id=id)
    # 수정할 내용을 대입
    todo.done = done
    # save는 기본키의 값이 있음녀 수정이고 없으면 삽입입니다.
    todo.save()

    # userid와 일치하는 데이터만 추출
    todos = Todo.objects.filter(userid=userid)

    # 결과 return
    return JsonResponse({"list":list(todos.values())})
  
  def delete(self, request):
    # 클라이언트의 데이터를 json형태로 가져오기
    request = json.loads(request.body)
    userid = request["userid"]
    id = request["id"]
    todo  = Todo.objects.get(id=id)
    #user를 확인해서 삭제
    if userid == todo.userid:
      todo.delete()
    # userid와 일치하는 데이터만 추출
    todos = Todo.objects.filter(userid=userid)
    #결과 리턴
    return JsonResponse({"list":list(todos.values())})
