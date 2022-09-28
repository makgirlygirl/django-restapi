from wsgiref import validate
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    questionID = serializers.IntegerField()
    passageID = serializers.IntegerField()
    question_type = serializers.IntegerField()
    question = serializers.CharField(max_length=1000)
    new_passage = serializers.CharField(max_length=2000)
    answer = serializers.CharField(max_length=100)
    d1 = serializers.CharField(max_length=100)
    d2 = serializers.CharField(max_length=100)
    d3 = serializers.CharField(max_length=100)
    d4 = serializers.CharField(max_length=100)

    def create(self, validated_data):
      return Question.objects.create(
        questionID=validated_data.get('questionID'),
        passageID=validated_data.get('passageID'),
        question_type=validated_data.get('question_type'),
        question=validated_data.get('question'),
        new_passage=validated_data.get('new_passage'),
        answer=validated_data.get('answer'),
        d1=validated_data.get('d1'),
        d2=validated_data.get('d2'),
        d3=validated_data.get('d3'),
        d4=validated_data.get('d4')
      )

    def update(self, instance, validated_data):
      instance.questionID=validated_data.get('questionID', instance.questionID)
      instance.passageID=validated_data.get('passageID', instance.passageID)
      instance.question_type=validated_data.get('question_type', instance.question_type)
      instance.question=validated_data.get('question', instance.question)
      instance.new_passage=validated_data.get('new_passage', instance.new_passage)
      instance.answer=validated_data.get('answer', instance.answer)
      instance.d1=validated_data.get('d1', instance.d1)
      instance.d2=validated_data.get('d2', instance.d2)
      instance.d3=validated_data.get('d3', instance.d3)
      instance.d4=validated_data.get('d4', instance.d4)
      instance.save()
      return instance
      
    class Meta:
        model = Question
        fields = ('questionID', 'passageID', 'question_type', 'question', 'new_passage','answer', 'd1', 'd2', 'd3', 'd4')


class GetQuestionsSerializer(serializers.ModelSerializer):
    qNum = serializers.IntegerField()
    qTypeList = serializers.ListField(
      child=serializers.BooleanField()
    )
      
    class Meta:
        model = Question
        fields = ('qNum', 'qTypeList')
