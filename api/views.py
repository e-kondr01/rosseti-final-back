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
    serializer_class = BadnaidProposalSerializer

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
    title = 'Введение измерителя NEW22 в снаряжение монтёров'
    description = (
        'По предложению Александра Александровича, работника Питерского'
        'филиала Россетей, в снаряжение электромонтёров был добавлен новый'
        'датчик NEW22,'
        'который уменьшил время выполнения обхода ЛЭП в среднем на'
        'полчаса в день.'
        'За своё предложение сотрудник получил 50 тысяч р.'
        )
    resp = {
        'title': title,
        'description': description
    }
    return JsonResponse(resp)


@api_view(['GET'])
def proposal_collection(request):
    title1 = 'Обход ЛЭП начиная с самой северной вышки'
    description1 = 'ЛЭП стоит обходить с самого севера, по Фен Шую'
    category1 = 'порядок выполнения служебного процесса'

    title2 = 'Введение измерителя NEW22 в снаряжение монтёров'
    description2 = (
        'Измеритель NEW22 позволяет уменьшить время'
        'выполнения обхода ЛЭП в среднем на полчаса за день'
        )
    category2 = 'снаряжение'

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
