
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),

    #REST FRAMEWORK URLS
    path('api/course/', include('courses.api.urls', 'course_api')),
    path('api/account/', include('account.api.urls', 'account_api')),
]
