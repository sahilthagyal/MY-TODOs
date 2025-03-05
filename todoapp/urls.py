from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('todolist/',views.todolist,name='todolist'),
    path('select-edit/',views.selectedit,name='select-edit'),
    path('select-delete/',views.selectdelete,name='select-delete'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('update/<int:pk>/',views.updatedata,name='updatedata'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('status/',views.status,name='status'),
]