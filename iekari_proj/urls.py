"""iekari_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from django.shortcuts import render
from django.urls import include, path
from django.contrib import admin 
from django.contrib.auth.decorators import login_required
from iekari.views.register import register_view, done_view #追加！
def index(request):
    contexts = {}
    return render(request,'index.html',contexts)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register_view, name='register'),
    path('accounts/register/done', done_view, name='register_done'), 
    path('iekari/', include('iekari.urls')),
]

