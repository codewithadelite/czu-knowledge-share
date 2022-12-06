"""
This file contains business logic for rest api that will be accessed
by c# window form
"""

import random

from drf_spectacular.utils import extend_schema, OpenApiExample

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from share.models import Task, User

from .serializers import TaskSerializer


class TaskList(APIView):
    """
    Class that contains functions to allow GET and POST HTTP requests
    """

    serializer_class = TaskSerializer
    permission_classes = [
        permissions.AllowAny,
    ]  # Allowing anybody to access this API without restriction

    @extend_schema(
        responses=TaskSerializer,
        examples=[
            OpenApiExample(
                "This is Task example that will be returned for client",
                summary="TASKS LIST ENDPOINT",
                description="This is Task example that will be returned for client",
                value={
                    "title": "Create new subject in system",
                    "description": "Create new subject called OBJECT MODELING with code ECD45C so students can be able to share files related to that subject.",
                    "assigned_to": "Brozek Jiri",
                    "status":"DONE",
                    "created_at": "2019-08-24T14:15:22Z",
                    "updated_at": "2019-08-24T14:15:22Z",
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
    )
    def get(self, request, format=None):
        """
        Endpoint which accept HTTP GET request and returns all assigned tasks.
        """

        tasks = Task.objects.all().order_by("-id")
        serializer = TaskSerializer(tasks, many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
		request=TaskSerializer,
	    examples = [
	         OpenApiExample(
	            'This is data example',
	            summary='TASKS ENDPOINT',
	            description='Example of json data that will be received from client',
	            value={
					 "title": "Create new subject in system",
                     "description": "Create new subject called OBJECT MODELING with code ECD45C so students can be able to share files related to that subject.",
	            },
	            request_only=True, # signal that example only applies to requests
	            response_only=False, # signal that example only applies to responses
	        ),
            OpenApiExample(
	            'This is data example',
	            summary='TASKS ENDPOINT',
	            description='Example of json data response to the client',
	            value={
					"title": "Create new subject in system",
                    "description": "Create new subject called OBJECT MODELING with code ECD45C so students can be able to share files related to that subject.",
                    "status":"PENDING",
                    "created_at": "2019-08-24T14:15:22Z",
					"updated_at": "2019-08-24T14:15:22Z"
                },
	            request_only=False, # signal that example only applies to requests
	            response_only=True, # signal that example only applies to responses
	        ),
	    ]
	)
    def post(self, request, format=None):
        """
        This endpoint receives information sent by HTTP POST request about the task in JSON format and then assign the 
        task to randomly admin selected by system.
        """

        task_data = request.data

        #QUERYING IDs OF ADMINS FOR SELECTING WHO TO ASSIGN TASK TO
        administrators_ids = [admin.id for admin in User.objects.filter(is_admin=True)]

        random_admin = random.choice(administrators_ids)
        task_data['user'] = random_admin

        serializer = TaskSerializer(data=task_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

