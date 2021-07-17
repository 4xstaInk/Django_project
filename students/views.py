from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        
        fullname = request.query_params.get('fullname', None)
        if fullname is not None:
            students = students.filter(fullname__icontains=fullname)
        
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse({'message': '{} students were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try: 
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist: 
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        student_serializer = StudentSerializer(student) 
        return JsonResponse(student_serializer.data) 
 
    elif request.method == 'PUT': 
        student_data = JSONParser().parse(request) 
        student_serializer = StudentSerializer(student, data=student_data) 
        if student_serializer.is_valid(): 
            student_serializer.save() 
            return JsonResponse(student_serializer.data) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        student.delete() 
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def student_list_published(request):
    students = Student.objects.filter(published=True)
        
    if request.method == 'GET': 
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)