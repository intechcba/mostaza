#The first part of the serializer class defines the fields that get serialized/deserialized.
# The create() and update() methods define how fully fledged instances are created
# or modified when calling serializer.save()

from rest_framework import serializers
from bismara.models import Doctor
from django.contrib.auth.models import User


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'reg_number', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #doctors = serializers.HyperlinkedRelatedField(many=True, view_name='doctor-detail', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
