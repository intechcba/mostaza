#The first part of the serializer class defines the fields that get serialized/deserialized.
# The create() and update() methods define how fully fledged instances are created
# or modified when calling serializer.save()

from rest_framework import serializers
from bismara.models import Doctor, User, UserState
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserState
        fields = ('description',)


class UserSerializer(serializers.ModelSerializer):
    state = UserStateSerializer(many=False, read_only=True, default=UserState("Pending"))
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'groups', 'state')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'reg_number', 'user')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        User.objects.create(**user_data)
        doctor = Doctor.objects.create(**validated_data)
        return doctor


