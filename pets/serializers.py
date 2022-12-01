from rest_framework import serializers
from pets.models import SexOptions, Pet
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexOptions.choices,
        default=SexOptions.DEFAULT,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True, read_only=True)