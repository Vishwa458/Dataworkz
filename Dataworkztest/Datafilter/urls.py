from django.conf.urls import url
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('stocks',views.StockView)
urlpatterns = [
                path('',include(router.urls))
              ]