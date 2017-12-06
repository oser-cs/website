"""Tutoring API serializers."""

from rest_framework import serializers
from tutoring.models import TutoringGroup


class TutoringGroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for TutoringGroup."""

    tutors = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:tutor-detail',
    )

    class Meta:  # noqa
        model = TutoringGroup
        fields = ('name', 'tutors',)
        extra_kwargs = {
            'url': {
                'view_name': 'api:tutoringgroup-detail',
            }
        }
