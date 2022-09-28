#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Question
from .serializers import QuestionSerializer, GetQuestionsSerializer

# Create your views here.

class QuestionListView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):
  
  def get(self, request, question_type=None):
    if question_type:
      try:
        queryset = Question.objects.filter(question_type=question_type)
      except Question.DoesNotExist:
        return Response({'errors': 'This question type item does not exist.'}, status=400)
      read_serializer = QuestionSerializer(queryset, many=True)
      return Response(read_serializer.data)

    else:    
      queryset = Question.objects.all()
      read_serializer = QuestionSerializer(queryset, many=True)
  
      return Response(read_serializer.data)

class QuestionPostView(
  APIView,
  UpdateModelMixin,
  DestroyModelMixin,
):

  def get(self, request):
    queryset = Question.objects.all()
    read_serializer = QuestionSerializer(queryset, many=True)

    return Response(read_serializer.data)

  def post(self, request):
    create_serializer = QuestionSerializer(data=request.data)

    if create_serializer.is_valid():

      question_item_object = create_serializer.save()
      read_serializer = QuestionSerializer(question_item_object)
      return Response(read_serializer.data, status=201)

    return Response(create_serializer.errors, status=400)

'''
  def put(self, request, id=None):
    try :
      question_item = Question.objects.get(id=id)

    except Question.DoesNotExist:
      return Response({'errors': 'This question item does not exist.'}, status=400)

    update_serializer = QuestionSerializer(question_item, data=request.data)

    if update_serializer.is_valid():
      question_item_object = update_serializer.save()
      read_serializer=QuestionSerializer(question_item_object)

      return Response(read_serializer.data, status=200)

    return Response(update_serializer.errors, status=400)
'''



