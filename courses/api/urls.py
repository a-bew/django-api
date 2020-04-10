from django.urls import path
from courses.api.views import (

    api_detail_course_view,
    api_update_course_view,
    api_delete_course_view,
    api_create_course_view,

)

app_name = 'course'

urlpatterns = [
    path('<language>/', api_detail_course_view, name='detail'),
        path('<language>/update', api_update_course_view, name='update'),
    path('<language>/delete', api_delete_course_view, name='delete'),
    path('create', api_create_course_view, name='create'),

]
