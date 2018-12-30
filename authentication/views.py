from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import Profile, StudentClass, Income

"""
request:
    path: '/user/'
    method: GET, POST, PUT, DELETE
    body: 'name: morteze, fname: pourkezemi'
    header: 'token: 1212'
response: 
    body: 'salam'    
    
    
"""


class ClassView(APIView):

    def get(self, request):
        student_classes = StudentClass.objects.all()
        json_student_class = []
        for student_class in student_classes:
            profiles = student_class.profile_set.all()
            json_profiles = []
            for profile in profiles:
                json_profiles.append({
                    'id': profile.id,
                    'name': profile.name,
                    'f_name': profile.f_name,
                    'age': profile.age,
                    'gender': 'man' if profile.gender else 'woman'
                })
            json_student_class.append({
                'id': student_class.id,
                'name': student_class.name,
                "profiles": json_profiles
            })

        return Response(json_student_class)


class UsersView(APIView):

    def get(self, request):
        profiles = Profile.objects.all()
        #profiles = Profile.objects.filter(student_class__id=2)
        json_profiles = []

        for profile in profiles:
            lesson_json = []

            for lesson in profile.lesson.all():
                lesson_json.append({
                    'id': lesson.id,
                    "name": lesson.name
                })
            json_profiles.append({
                'id': profile.id,
                'name': profile.name,
                'f_name': profile.f_name,
                'age': profile.age,
                'gender': 'man' if profile.gender else 'woman',
                'class': {
                    'id': profile.student_class.id,
                    'name': profile.student_class.name
                },
                "lessons": lesson_json,
                "income": profile.income.mounthly_income if hasattr(self, "income") else None
            })

        return Response(json_profiles)

    def post(self, request):

        try:
            name = str(request.data['name'])
            family_name = str(request.data['family_name'])
            age = int(request.data.get('age', 0))
            gender = bool(request.data.get('gender', True))

        except(ValueError, KeyError):
            return Response({'error': 'data is incorrect'}, status=400)

        # profile = Profile()
        # profile.name = name
        # profile.f_name = family_name
        # profile.age = age
        # profile.gender = gender
        # Profile.save()

        profile = Profile.objects.create(
            name=name,
            f_name=family_name,
            age=age,
            gender=gender
        )
        Income.objects.create(
            profile=profile,
            income=100,
            mounthly_income=2700
        )
        return Response({
            "massage": "profile is created"
        })


class UserView(APIView):

    def put(self, request, profile_id):

        try:
            name = str(request.data.get('name', ''))
            family_name = str(request.data.get('family_name', ''))
            age = int(request.data.get('age', 0))
            gender = (request.data.get('gender'))

            if gender:
                gender = bool(gender)

        except(ValueError, KeyError):
            return Response({'error': 'data is incorrect'}, status=400)

        try:
            profile = Profile.objects.get(id = profile_id)
        except(Profile.DoesNotExist()):
            return Response({
                "message": "profile is not excist"
            })
        if name:
            profile.name = name

        if family_name:
            profile.f_name = family_name

        if age:
            profile.age = age

        if gender is not None:
            profile.gender = gender

        profile.save()
        return Response({
            "massage": "profile "+str(profile_id)+" is edited"
        })

    def delete(self, request, profile_id):
        # try:
        #     profile = Profile.objects.get(id = profile_id)
        # except(Profile.MultipleObjectsReturned, Profile.DoesNotExist):
        #     return Response({
        #         "massage": "not exist"
        #     }, status=404)
        # profile.delete()
        if not Profile.objects.filter(id=profile_id).exists():
            return Response({
                "massage": " not exists"
            }, status=404)
        Profile.objects.filter(id=profile_id).delete()
        return Response({
            'message': 'profile '+str(profile_id)+' is deleted'
        })
