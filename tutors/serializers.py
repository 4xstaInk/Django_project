from rest_framework import serializers 
from tutors.models import Tutor
from students.models import Field
from students.serializers import StudentSerializer


class TutorSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()

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
                  'sex', "students")

    def get_students(self, obj):
        field = Field.objects.get(id=obj.field.id)
        students = StudentSerializer(field.student_set.all(), many=True).data
        return students


class SecondaryTutorSerializer(serializers.ModelSerializer):

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
                  'sex',)


