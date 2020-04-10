
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from courses.models import Course
from courses.api.serializers import CourseSerializer
from django.contrib.auth.models import User
from account.models import Account

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_detail_course_view(request, language):
    try:
        course = Course.objects.get(language=language.title())
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)

@api_view(['PUT', ])

@permission_classes((IsAuthenticated, ))
def api_update_course_view(request, language):
    try:
        course = Course.objects.get(language=language.title())
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to edit that."})

    if request.method == "PUT":
        serializer = CourseSerializer(course, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_delete_course_view(request, language):
    try:
        course = Course.objects.get(language=language.title())
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to edit that."})

    if request.method == "DELETE":
        operation = course.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def api_create_course_view(request):

    account = request.user
    # if blog_post.author != current_user:
    #     return Response({'response': "You don't have permission to edit that."})

#    user = Account.objects.get(pk=current_user)

    course = Course(author = account)
#    course = Course.objects.get(language=language.title())
    if request.method == "POST":
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    