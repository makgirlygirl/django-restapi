from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Passage

class PassageSerializer(serializers.ModelSerializer):
    passageID = serializers.IntegerField()
    passage = serializers.CharField(max_length=2000, required=True)

    def create(self, validated_data):
      return Passage.objects.create(
        passageID=validated_data.get('passageID'),
        passage=validated_data.get('passage')
      )

    def update(self, instance, validated_data):
      instance.passageID = validated_data.get('passageID', instance.passageID)
      instance.passage = validated_data.get('passage', instance.passage)
      instance.save()
      return instance

    class Meta:
        model = Passage
        fields = ('passageID', 'passage')