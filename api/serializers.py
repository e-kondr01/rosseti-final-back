from rest_framework import serializers

from .models import *


class ProposalDraftSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = ProposalDraft
        fields = ['id', 'description', 'author']


class ProposalSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    moderator = serializers.PrimaryKeyRelatedField(
        read_only=True, required=False)

    class Meta:
        model = Proposal
        fields = [
            'id', 'title', 'description', 'status', 'author', 'moderator',
            'created_at'
            ]


class ProposalSerializerForList(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = [
            'id', 'title',
            ]
