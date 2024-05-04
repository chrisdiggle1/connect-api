from rest_framework import generics, permissions, filters
from .models import Event
from .serializers import EventSerializer
from connect_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count


class EventList(generics.ListCreateAPIView):
    """
    Lists events or allows users to create an event if logged in.
    The perform_create method associates the event with the logged-in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        interested_count=Count('interested', distinct=True),
        going_count=Count('attending', distinct=True),
        review_count=Count('reviews', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'interested__owner__profile': ['exact'],
        'attending__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'category': ['exact'],
        'event_date': ['lte'],
    }
    search_fields = [
        'owner__username',
        'title',
        'event_date',
    ]
    ordering_fields = [
        'comments_count',
        'interested_count',
        'attending_count',
        'review_count',
        'interested__created_at',
        'attending__created_at',
        'event_date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, or deletes an event by ID if the user owns it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        interested_count=Count('interested', distinct=True),
        attending_count=Count('attending', distinct=True),
        review_count=Count('reviews', distinct=True),
    ).order_by('-created_at')
