from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField


class Employee(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE,
                         related_name='employee')
    name = CharField(max_length=64)
    surname = CharField(max_length=64)
    post = CharField(max_length=128)
    experience = CharField(max_length=128)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class ProposalDraft(models.Model):
    description = models.TextField()
    author = models.ForeignKey(Employee, on_delete=models.CASCADE,
                               related_name='proposal_drafts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Предложение от {self.author}'


class Proposal(models.Model):
    draft = models.OneToOneField(ProposalDraft, on_delete=models.CASCADE,
                                 related_name='draft')
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=128)
    category = models.CharField(max_length=128, blank=True)
    author = models.ForeignKey(Employee, on_delete=models.CASCADE,
                               related_name='authored_proposals')
    moderator = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                  related_name='moderated_proposals',
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Обработанное предложение от {self.author}'
