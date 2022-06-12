from django.urls import path, include
from .views import BusinessUnitView, UserView, MillView,\
    ShiftView, TaskView, TaskHandoverView, PositionView

urlpatterns = [
    path('businessunit/', BusinessUnitView.as_view()),
    path('businessunit//<int:id>', BusinessUnitView.as_view()),
    path('user/', UserView.as_view()),
    path('user//<int:id>', UserView.as_view()),
    path('mill/', MillView.as_view()),
    path('mill//<int:id>', MillView.as_view()),
    path('shift/', ShiftView.as_view()),
    path('shift//<int:id>', ShiftView.as_view()),
    path('task/', TaskView.as_view()),
    path('task//<int:id>', TaskView.as_view()),
    path('taskhandover/', TaskHandoverView.as_view()),
    path('taskhandover//<int:id>', TaskHandoverView.as_view()),
    path('position/', PositionView.as_view()),
    path('position//<int:id>', PositionView.as_view())
]