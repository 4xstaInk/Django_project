from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    tutors = serializers.SerializerMethodField()

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
                  'sex',
                  'tutors'
                  )

    def get_tutors(self, obj):
        from tutors.serializers import SecondaryTutorSerializer
        tutors = []
        for field in obj.field.all():
            temp = SecondaryTutorSerializer(field.tutor_set.all(), many=True).data
            tutors.append(temp)
        return tutors[0]
