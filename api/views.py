from django.contrib.auth.models import Group
from rest_framework import generics

from .serializers import *
from .models import *


class ProposalDraftView(generics.ListCreateAPIView):
    serializer_class = ProposalDraftSerializer
    queryset = ProposalDraft.objects.none()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProposalListView(generics.ListCreateAPIView):
    serializer_class = ProposalSerializerForList

    def get_queryset(self):
        user = self.request.user
        moderators = Group.objects.get(name='moderators')
        if moderators in user.groups.all():
            return Proposal.objects.all()
        else:
            return Proposal.objects.filter(author=user)


class ProposalView(generics.RetrieveUpdateAPIView):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Proposal.objects.filter(author=user)
