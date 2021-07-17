from rest_framework import serializers 
from tutors.models import Tutor
from students.serializers import StudentSerializer
 
class TutorSerializer(serializers.ModelSerializer):
    
    students = StudentSerializer(many=True, read_only = True)
    class Meta:
        model = Tutor
        fields = ('id',
                  'age',
                  'courses',
                  'email',
                  'field',
                  'fullname',
                  'marital_status',
                  'nationality',
                  'sex')