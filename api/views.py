from django.contrib.auth.models import Group
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import *
from .models import *


class ProposalDraftView(generics.CreateAPIView):
    serializer_class = ProposalDraftSerializer
    queryset = ProposalDraft.objects.none()

    def perform_create(self, serializer):
        draft = serializer.save(author=self.request.user.employee)
        proposal = Proposal(draft=draft, status='sent to moderator',
                            author=self.request.user.employee)
        proposal.save()


class ProposalListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProposalSerializerForList

    def get_queryset(self):
        user = self.request.user
        moderators = Group.objects.get(name='moderators')
        if moderators in user.groups.all():
            return Proposal.objects.all()
        else:
            return Proposal.objects.filter(author=user.employee)


class ProposalView(generics.RetrieveUpdateAPIView):
    serializer_class = ProposalSerializerForRetrieveUpdate

    def get_queryset(self):
        user = self.request.user
        moderators = Group.objects.get(name='moderators')
        if moderators in user.groups.all():
            return Proposal.objects.all()
        else:
            return Proposal.objects.filter(author=user.employee)

    def perform_update(self, serializer):
        instance = serializer.save(moderator=self.request.user.employee)
