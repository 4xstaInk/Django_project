from rest_framework import serializers 
from tutors.models import Tutor


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
        from students.models import Field
        from students.serializers import SecondaryStudentSerializer

        field = Field.objects.get(name=obj.field)

        students = SecondaryStudentSerializer(field.student_set.all(), many=True).data

        return students



