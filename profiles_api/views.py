from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'nesto nesto',
            'isto tako nesto',
            'jos i ovo'
        ]
        return Response({'message': 'jeste', 'an_apiview': an_apiview})