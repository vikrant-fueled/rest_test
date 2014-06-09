# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    '''

    List of api endpoints for this Project.

    ### Authentication

    Visit auth-token's url to obtain a JSON-Web Token. `BasicAuth` is also supported.

    ### Errors

    By default all error responses will include a key `details` in the body of
    the response.

    '''
    return Response({
        'api_root': reverse('api_root', request=request, format=format),
        'user': reverse('api_user', request=request, format=format),
        'auth-token': reverse('api_auth_token', request=request, format=format),
    })


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    '''
    Endpoint to get and update profile of a `User`.
    '''
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
