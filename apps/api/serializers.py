from rest_framework import serializers
from .models import User, BusinessUnit, Mill, Position, Shifts, Task, TaskHandover


class TaskHandoverSerializer(serializers.ModelSerializer):
    task = serializers.CharField()
    handover_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    handover_pic = serializers.CharField(max_length = 125)
    handover_remark = serializers.CharField()
    handover_assigned_by = serializers.IntegerField()
    created_by = serializers.CharField(max_length = 125)
    created_date =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta: 
        model = TaskHandover
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    task = serializers.CharField(max_length=500)
    assigned_to = serializers.CharField(max_length=500)
    assigned_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    shift = serializers.CharField(max_length=250)
    start_date =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_date =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    due_date =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    location = serializers.CharField(max_length=250)
    comment = serializers.CharField()
    remarks = serializers.CharField()
    progress = serializers.CharField(max_length=250)
    photo = serializers.CharField()
    photo_varying = serializers.CharField()
    assigned_by = serializers.CharField(max_length = 500)
    is_handover = serializers.BooleanField()
    created_by = serializers.CharField(max_length=500)
    created_date =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    type = serializers.CharField(max_length = 250)
    mill = serializers.CharField()
    time_incident =  serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Task
        fields = ('__all__')



class ShiftSeriallizer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 125)
    shift = serializers.IntegerField()
    user = serializers.CharField()

    class Meta:
        model = Shifts
        fields = ('__all__')

class BUSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(max_length = 125) # PLEASE FOLLOW THE NAME IN MODELSSSSS

    class Meta: 
        model = BusinessUnit
        fields = ('__all__')


class PositionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length = 500)
    created_by = serializers.CharField(max_length=125)
    created_date = serializers.DateField()

    class Meta:
        model = Position
        fields = ('__all__')

class MillSerializer(serializers.ModelSerializer):
    mill_name = serializers.CharField(max_length=125)
    business_unit = serializers.CharField()

    class Meta:
        model = Mill
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=125)
    email = serializers.CharField(max_length=125)
    contact = serializers.CharField(max_length=125)
    mill = serializers.CharField()
    position = serializers.CharField()

    class Meta:
        model = User
        fields=('name', 'email', 'contact', 'mill', 'position')

    # def get_mill(self, obj):
    #     user_mills = []
    #     millobjs = Mill.objects.all()
    #     for mill in millobjs:
    #         user_mills.append({'Mill Name': mill.mill_name})
    #     return user_mills

    # def get_position(self, obj):
    #     user_positions = []
    #     pos_objs = Position.objects.all()
    #     for position
