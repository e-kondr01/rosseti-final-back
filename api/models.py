from django.contrib.auth.models import User
from django.db import models


class ProposalDraft(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='proposal_drafts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Предложение от {self.author}'


class Proposal(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.CharField(max_length=128)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='proposals')
    moderator = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='moderated_proposals')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Обработанное предложение от {self.author}'
