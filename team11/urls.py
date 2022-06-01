"""team11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 이거 밑줄 오류난 거 해결한 사이트:
# https://qiita.com/startours777/items/552b6ae5a3ed2915406a




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('team11app.urls')) # https://localhost/로 가는 길~
]

# 장고 실행 : py manage.py runserver 12000
# 장고 외부에서 접속하기 : 
# 1. py manage.py runserver 0.0.0.0:12000
# 2. settings.py가서 ALLOWED_HOSTS에 접속허용할 외부ip 문자열로 입력 ex)'123.456.789'
