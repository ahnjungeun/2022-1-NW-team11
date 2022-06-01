from django.urls import path, include
from team11app import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create), # 끝에 /붙이기
    # 2번째 인자로 view 정보 넣어줘야 함 
    # 아니면 에러남 TypeError: _path() missing 1 required positional argument: 'view'
    # path('show/<answer>', views.show), # <answer> 이름이 answer인 값이 가변적으로 들어옴
    

]

# 장고 실행 : py manage.py runserver 12000
