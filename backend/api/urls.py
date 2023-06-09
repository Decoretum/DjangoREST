from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('ModelData', views.modelData),
    path('APIView', views.APIView),
    path('PostView', views.PostView),
    path('TestPostView', views.TestPostView)

]