from rest_framework import generics, permissions
from connect_api.permissions import IsOwnerOrReadOnly
from interested.models import Interested
from interested.serializers import InterestedSerializer


class InterestedList(generics.ListCreateAPIView):
    """
    Lists or creates expressions of interest in events.
    The perform_create method associates the interest with the logged-in user.
    """
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InterestedDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or deletes an interest in an event by ID if the user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InterestedSerializer
    queryset = Interested.objects.all()