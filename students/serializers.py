from rest_framework import serializers
from students.models import Student, Field


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ("name",)


class StudentSerializer(serializers.ModelSerializer):
    tutors = serializers.SerializerMethodField()
    fields = FieldSerializer(many=True)

    class Meta:
        model = Student
        fields = ('id',
                  'title',
                  'fullname',
                  'email',
                  'fields',
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
        from tutors.serializers import TutorSerializer
        from tutors.models import Tutor
        student_fields = obj.fields.all()
        tutors = []
        for field in student_fields:
            temp = TutorSerializer(Tutor.objects.filter(field__iexact=field.name), many=True).data
            tutors.append(temp)
        return tutors[0]


class SecondaryStudentSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Student
        fields = ('id',
                  'title',
                  'fullname',
                  'email',
                  'fields',
                  'student_id_number',
                  'year_enrolled',
                  'age',
                  'marital_status',
                  'nationality',
                  'description',
                  'sex',
                  )
