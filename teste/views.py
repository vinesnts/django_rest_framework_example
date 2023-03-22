from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def teste(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        return Response(data={
            'status': 'testou GET'
        })

    elif request.method == 'POST':
        data=request.data
        return Response(data={
            'status': 'testou POST',
            'payload': data
        })