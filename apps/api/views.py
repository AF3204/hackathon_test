from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import BUSerializer, UserSerializer, MillSerializer, PositionSerializer, ShiftSeriallizer, TaskSerializer, TaskHandoverSerializer
from .models import BusinessUnit, Mill, User, Shifts, Task, TaskHandover, Position


class BusinessUnitView(APIView):
    queryset = BusinessUnit.objects.all()
    serializer_class =BUSerializer
    def get(self, request, id=None):
        if id:
            businessunit = BusinessUnit.objects.get(id=id)
            serializer = BUSerializer(businessunit)
            return Response({'status': 'success',
            'businessUnit': serializer.data}, 
            status= status.HTTP_200_OK)

        businessunits = BusinessUnit.objects.all()
        serializer = BUSerializer(businessunits, many=True)
        return Response({'status': 'success',
            'businessUnit': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BUSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        businessunit = BusinessUnit.objects.get(id=id)
        serializer = BUSerializer(businessunit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self,request, id=None):
        businessunit = get_object_or_404(BusinessUnit, id=id)
        businessunit.delete()
        return Response({'status': 'success', 'data': "Business Unit deleted"})


class UserView(APIView):
    def get(self, request, id= None):
        if id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response({'status': 'success',
            'user': serializer.data}, 
            status= status.HTTP_200_OK)

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'status': 'success',
            'user': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        user =  User.objects.get(id=id)
        serializer = BUSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({'status': 'success', 'data': "User deleted"})


class MillView(APIView):
    def get(self, request, id=None):
        if id:
            mill = Mill.objects.get(id=id)
            serializer = MillSerializer(mill)


            return Response({'status': 'success',
            'mill': serializer.data}, 
            status= status.HTTP_200_OK)

        mills = Mill.objects.all()
        serializer = MillSerializer(mills, many=True)
        return Response({'status': 'success',
            'mill': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MillSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        mill =  Mill.objects.get(id=id)
        serializer = MillSerializer(mill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        user = get_object_or_404(Mill, id=id)
        user.delete()
        return Response({'status': 'success', 'data': "Mill deleted"})



class ShiftView(APIView):
    def get(self, request, id=None):
        if id:
            shift = Shifts.objects.get(id=id)
            serializer = ShiftSeriallizer(shift)
            return Response({'status': 'success',
            'shift': serializer.data}, 
            status= status.HTTP_200_OK)

        shifts = Shifts.objects.all()
        serializer = ShiftSeriallizer(shifts, many=True)
        return Response({'status': 'success',
            'shift': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShiftSeriallizer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id=None):
        shift =  Shifts.objects.get(id=id)
        serializer = ShiftSeriallizer(shift, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        shift = get_object_or_404(Shifts, id=id)
        shift.delete()
        return Response({'status': 'success', 'data': "Shift deleted"})


class TaskView(APIView):
    def get(self, request, id=None):
        if id:
            task = Task.objects.get(id=id)
            serializer = TaskSerializer(task)
            return Response({'status': 'success',
            'task': serializer.data}, 
            status= status.HTTP_200_OK)

        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'status': 'success',
            'task': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        task =  Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({'status': 'success', 'data': "Shift deleted"})


class TaskHandoverView(APIView):
    def get(self, request, id=None):
        if id:
            taskhandover = TaskHandover.objects.get(id=id)
            serializer = TaskHandoverSerializer(taskhandover)
            return Response({'status': 'success',
            'handover': serializer.data}, 
            status= status.HTTP_200_OK)

        taskhandovers = TaskHandover.objects.all()
        serializer = TaskHandoverSerializer(taskhandovers, many=True)
        return Response({'status': 'success',
            'handover': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskHandoverSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        taskhandover =  TaskHandover.objects.get(id=id)
        serializer = TaskHandoverSerializer(taskhandover, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        taskhandover = get_object_or_404(TaskHandover, id=id)
        taskhandover.delete()
        return Response({'status': 'success', 'data': "Handover Task deleted"})

class PositionView(APIView):
    def get(self, request, id=None):
        if id:
            position = Position.objects.get(id=id)
            serializer = PositionSerializer(Position)
            return Response({'status': 'success',
            'position': serializer.data}, 
            status= status.HTTP_200_OK)

        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response({'status': 'success',
            'position': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PositionSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'status': 'success', "data": serializer.data}, 
            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, 
            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        position =  Position.objects.get(id=id)
        serializer = PositionSerializer(position, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'modified_data': serializer.data})
        else:
            return Response({'status':'error','unmodified_data': serializer.data})

    def delete(self, request, id=None):
        position = get_object_or_404(Position, id=id)
        position.delete()
        return Response({'status': 'success', 'data': "Handover Task deleted"})




    

    
            
        