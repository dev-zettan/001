from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from app.views import Task01ViewSet, Task02ListView
from app.views import Task02CreateView
from app.views import Task03view

router = routers.DefaultRouter()
router.register('task01', Task01ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('task02/', Task02ListView.as_view(), name='tas2'),
    path('task02create/', Task02CreateView.as_view, name='tas2'),
    path('task03/', Task03view.as_view(), name='tas3'),
]