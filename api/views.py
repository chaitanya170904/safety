from rest_framework.decorators import api_view
from rest_framework.response import Response
from detoxify import Detoxify
from .serializers import TweetSerialzer

model = Detoxify('unbiased')

@api_view(['POST'])
def check_tweet(request):
    serializer = TweetSerialzer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        results = model.predict(text)
        is_appropriate = results['toxicity'] < 0.5
        response = {
            'is_appropriate': is_appropriate,
            'scores': results
        }
        return Response(response)
    else:
        return Response(serializer.errors, status=400)
