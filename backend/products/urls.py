from django.urls import path, include, re_path
#from django.conf.urls import url
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r"ProductList", ProductRound, basename='list'),
# router.register(r"<int:pk>/",ProductRound, basename='detail')

urlpatterns = [
    path('<int:pk>/', ProductMixinView.as_view()),
    path('CreateProduct/<int:pk>/', ProductMixinView.as_view()),
    path('', ProductListCreateAPIView.as_view()),
    path('ProductList', ProductMixinView.as_view()),
    path('UpdateProduct/<int:pk>/', ProductMixinView.as_view()),
    path('DeleteProduct/<int:pk>/', ProductMixinView.as_view()),
    #re_path(r'^api/', include(router.urls))
]
#urlpatterns = router.urls