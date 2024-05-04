from rest_framework import generics, permissions
from connect_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ReviewList(generics.ListCreateAPIView):
    """
    Lists reviews or allows users to create a review if logged in.
    The perform_create method associates the review with the logged-in user.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['event']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves, updates, or deletes a review by ID if the user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
