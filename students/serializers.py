from rest_framework import serializers 
from students.models import Student
from tutors.serializers import TutorSerializer
 
class StudentSerializer(serializers.ModelSerializer):
    
    tutors = TutorSerializer(many=True, read_only = True)
    class Meta:
        model = Student
        fields = ('id',
                  'title',
                  'fullname',
                  'email',
                  'field',
                  'student_id_number',
                  'year_enrolled',
                  'age',
                  'marital_status',
                  'nationality',
                  'description',
                  'sex'
                  )