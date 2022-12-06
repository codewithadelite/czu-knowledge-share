from pyexpat import model
from rest_framework import serializers
from share.models import Task


class TaskSerializer(serializers.ModelSerializer):

    assigned_to = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ["title", "description", "assigned_to", "status", "user", "created_at", "updated_at"]

    def get_assigned_to(self, obj):
        """
        Getting the name of the admin task is assigned to
        """

        return "{lname} {fname}".format(
            lname=obj.user.administrator.last_name,
            fname=obj.user.administrator.first_name,
        )

    def get_status(self, obj):
        """
        Getting the status of the task(DONE or PENDING)
        """

        if obj.is_done == True:
            return "DONE"
        return "PENDING"
