from django.contrib.auth.models import Group
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view

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


@api_view(['GET'])
def latest_successful_proposal(request):
    title = 'test title'
    description = 'Test description'
    resp = {
        'title': title,
        'description': description
    }
    return JsonResponse(resp)


@api_view(['GET'])
def proposal_collection(request):
    title1 = 'test title'
    description1 = 'Test description'
    category1 = 'test category'
    title2 = 'test title'
    description2 = 'Test description'
    category2 = 'test category'

    resp = [
        {
            'title': title1,
            'category': category1,
            'description': description1
            },
        {
            'title': title2,
            'category': category2,
            'description': description2
            },
    ]
    return JsonResponse(resp)
