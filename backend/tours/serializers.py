from rest_framework.serializers import ModelSerializer

from tours.models import Tour


class TourSerializer(ModelSerializer):
    class Meta:
        model = Tour
        fields = ['title', 'city', 'count_comment']
