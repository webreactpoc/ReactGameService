from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # GET ALL
    path('get/tests/', views.GET_test, name='GET_ALL_TEST'),
    path('get/testees/', views.GET_testee, name='GET_ALL_TESTEE'),
    path('get/statuss/', views.GET_status, name='GET_ALL_STATUS'),
    path('get/organisations/', views.GET_organisation, name='GET_ALL_ORGANISATION'),
    path('get/attempts/', views.GET_attempt, name='GET_ALL_ATTEMPT'),

    # GET BY ID
    path('get/test/<int:id>', views.GET_test, name='GET_TEST_BY_ID'),
    path('get/testee/<int:id>', views.GET_testee, name='GET_TESTEE_BY_ID'),
    path('get/status/<int:id>', views.GET_status, name='GET_STATUS_BY_ID'),
    path('get/organisation/<int:id>', views.GET_organisation, name='GET_ORGANISATION_BY_ID'),
    path('get/attempt/<int:id>', views.GET_attempt, name='GET_ATTEMPT_BY_ID'),

    # POST NEW 
    path('post/test/', views.POST_test, name='POST_NEW_TEST'),
    path('post/testee/', views.POST_testee, name='POST_NEW_TESTEE'),
    path('post/status/', views.POST_status, name='POST_NEW_STATUS'),
    path('post/organisation/', views.POST_organisation, name='POST_NEW_ORGANISATION'),
    path('post/attempt/', views.POST_attempt, name='POST_NEW_ATTEMPT'),
]