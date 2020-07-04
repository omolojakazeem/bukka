from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):

    def get(self,request):
        content = "Welcome"
        return Response(content)
