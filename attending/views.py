from rest_framework import generics, permissions
from connect_api.permissions import IsOwnerOrReadOnly
from attending.models import Attending
from attending.serializers import AttendingSerializer


class AttendingList(generics.ListCreateAPIView):
    """
    Lists or creates attendance posts for events.
    The perform_create method associates the post with the logged-in user.
    """
    serializer_class = AttendingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Attending.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AttendingDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or deletes an attendance post by ID if the user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendingSerializer
    queryset = Attending.objects.all()
