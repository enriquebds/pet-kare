from rest_framework import serializers
from pets.models import SexOptions, Pet
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from groups.models import  Group
from traits.models import Trait


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
    traits = TraitSerializer(many=True)

    def create(self, validated_data: dict) -> Pet:

        trait_dict = validated_data.pop("traits")
        group_dict = validated_data.pop("group")
        group, _ = Group.objects.get_or_create(**group_dict)

        pet_obj = Pet.objects.create(**validated_data, group=group)

        for trait in trait_dict:
            trait, _ = Trait.objects.get_or_create(**trait)
            pet_obj.traits.add(trait)

        return pet_obj

    def update(self, instance: Pet, validated_data: dict):
        group_dict: dict = validated_data.pop("group", None)


        if group_dict:
            group_obj, created = Group.objects.get_or_create(pet=instance)

            for key, value in group_dict.items():
                setattr(group_obj, key, value)
            group_obj.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
