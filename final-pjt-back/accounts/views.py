from django.shortcuts import get_object_or_404
from dj_rest_auth.registration.views import RegisterView
from .serializers import UserUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
# Create your views here.
# class CustomRegisterView(RegisterView):
#     serializer_class = CustomRegisterSerializer

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def userupdate(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    serializer = UserUpdateSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def signout(request):
  request.user.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)