from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import DownloadCounter
from .serializers import DownloadCounterSerializer

@api_view(['POST'])
def increment_download(request):
    name = request.data.get('name', 'default')

    counter, created = DownloadCounter.objects.get_or_create(name=name)
    counter.count = F('count') + 1
    counter.save()
    counter.refresh_from_db()

    serializer = DownloadCounterSerializer(counter)
    return Response(serializer.data, status=status.HTTP_200_OK)
