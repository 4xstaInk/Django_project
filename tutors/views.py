
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutors.models import Tutor
from tutors.serializers import TutorSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutor_list(request):
    if request.method == 'GET':
        tutors = Tutor.objects.all()
        
        fullname = request.query_params.get('fullname', None)
        if fullname is not None:
            tutors = tutors.filter(fullname__icontains=fullname)
        
        tutors_serializer = TutorSerializer(tutors, many=True)
        return JsonResponse(tutors_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutor_data = JSONParser().parse(request)
        tutor_serializer = TutorSerializer(data=tutor_data)
        if tutor_serializer.is_valid():
            tutor_serializer.save()
            return JsonResponse(tutor_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutor.objects.all().delete()
        return JsonResponse({'message': '{} Tutors were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutor_detail(request, pk):
    try: 
        tutor = Tutor.objects.get(pk=pk) 
    except Tutor.DoesNotExist: 
        return JsonResponse({'message': 'The tutor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutor_serializer = TutorSerializer(tutor)
        return JsonResponse(tutor_serializer.data)
 
    elif request.method == 'PUT': 
        tutor_data = JSONParser().parse(request) 
        tutor_serializer = TutorSerializer(tutor, data=tutor_data) 
        if tutor_serializer.is_valid(): 
            tutor_serializer.save() 
            return JsonResponse(tutor_serializer.data) 
        return JsonResponse(tutor_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutor.delete() 
        return JsonResponse({'message': 'Tutor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def tutor_list_published(request):
    tutors = Tutor.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutors_serializer = TutorSerializer(tutors, many=True)
        return JsonResponse(tutors_serializer.data, safe=False)