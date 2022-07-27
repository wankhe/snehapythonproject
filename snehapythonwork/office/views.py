from http import server
from socket import J1939_EE_INFO_NONE
from django.http import JsonResponse
from .models import office
from .serializer import officeserializer
from rest_framework.decoraters import  api_views
from rest_framework.responce import Responce
from rest_framework.responce import status


@api_view(['GET', 'POST'])
def office_list(request):
    
    if request.method =='GET':
    
    #to get all inputes 
    # to serialize them
    # and to get json responce
    
    
         office = Office.object.all()
    
          serializer = officeserializer(office, many=True)
          return JsonResponse({"office":serializer.data}, safe=False)
      
       if request.method =='POST':
           
           serializer = Officeserializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Responce(serializer.data, status=status.HTTP_201_CREATED)
               

@api_veiw(['GET', 'PUT', 'DELETE'])
def office_details(request, id):
    
    try:

       office.objects.get(pk=id)
    except Office.DoesnotExist:
        return Responce(status=status.Http_404_NOT_FOUND)

    
    
    if request.method =='GET':
        serializer = officeserializer(office)
        return Responce(serializer.data)
    elif request.method == 'POST':
        serializer = officeserializer(office, data=request.data)
        if serializer is valid():
            serializer.save()
            return Responce(serializer.data)
        return Responce(serializer.errors, status=status.HTTP_400_BAD_REQUEST_CREATED)

        
    elif request.method == 'DELETE':
        office.delete()
        return Responce(status=status.HTTP_204 _NO_CREATED)
    
    