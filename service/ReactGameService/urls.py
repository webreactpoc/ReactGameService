from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # GET ALL
    path('get/tests/', views.GET_test, name='test'),
    path('get/testees/', views.GET_testee, name='testee'),
    path('get/statuss/', views.GET_status, name='status'),
    path('get/organisations/', views.GET_organisation, name='organisation'),
    path('get/attempts/', views.GET_attempt, name='attempt'),

    # GET Y ID
    path('get/test/<int:id>', views.GET_test, name='test'),
    path('get/testee/<int:id>', views.GET_testee, name='testee'),
    path('get/status/<int:id>', views.GET_status, name='status'),
    path('get/organisation/<int:id>', views.GET_organisation, name='organisation'),
    path('get/attempt/<int:id>', views.GET_attempt, name='attempt'),
    
    path('post/test/', views.POST_test, name='test'),
    path('post/testee/', views.POST_testee, name='testee'),
    path('post/status/', views.POST_status, name='status'),
    path('post/organisation/', views.POST_organisation, name='organisation'),
    path('post/attempt/', views.POST_attempt, name='attempt'),
]