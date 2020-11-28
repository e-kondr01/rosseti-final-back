from rest_framework import serializers

from .models import *


class ProposalDraftSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    class Meta:
        model = ProposalDraft
        fields = ['id', 'description', 'author']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'id', 'name', 'surname',
            'post', 'experience'
            ]


class ProposalSerializerForRetrieveUpdate(serializers.ModelSerializer):
    author = EmployeeSerializer(read_only=True)
    moderator = EmployeeSerializer(read_only=True)
    draft = serializers.SlugRelatedField(
        read_only=True,
        slug_field='description'
    )

    class Meta:
        model = Proposal
        fields = [
            'id', 'draft', 'title', 'description', 'status', 'author',
            'moderator',
            'created_at', 'updated_at'
            ]
        read_only_fields = ['author', 'moderator', 'created_at', 'updated_at']


class ProposalSerializerForList(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = [
            'id', 'title', 'status',
            ]
