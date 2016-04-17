from django.contrib.auth.models import User
from bismara.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from bismara.models import Doctor
from bismara.serializers import DoctorSerializer
from bismara.permissions import *
from rest_framework import renderers
from rest_framework.decorators import detail_route


#The ONLY EntryPoint. This is great :)
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'doctors': reverse('doctor-list', request=request, format=format)
    })


class DoctorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    #
    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     doctor = self.get_object()
    #     return Response(doctor.highlighted)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#For READ ONLY viewset use viewsets.ReadOnlyModelViewSet
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save()

