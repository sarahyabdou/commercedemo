from rest_framework import views
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from product.models import *
from .serlizer import * 
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
####baseclass
class allc(APIView):
    def get(self,request):

        data=Product.Getall()
        datajson=Productserlizer(data,many=True).data
     
        return Response({'msg':'acceptdata cu developers','data':datajson})
    
    
##generic
class allg(ListAPIView):
    serializer_class=Productserlizer
    queryset=Product.Getall()
@api_view(['GET'])
def Hello(request):
    
    return Response({'msg':'hello cu developers'})
@api_view(['GET','POST'])
def acceptdata(request):
    # print(request.data)
    return Response({'msg':'acceptdata cu developers','data':request.data})
@api_view(['GET'])
def all(request):
     data=Product.Getall()
     datajson=Productserlizer(data,many=True).data
     
     return Response({'msg':'acceptdata cu developers','data':datajson})
@api_view(['GET'])
def detail(request,id):
    data=Product.getproductdetails(id)

    datajson=Productserlizer(data).data
    return Response({'data':datajson})
from rest_framework import status

@api_view(['POST'])
def add(request):
    obj=Productserlizer(data=request.data)
    if(obj.is_valid()):
        obj.save()
        return Response({'msg':'data accept'})
    return Response({'msg':' wrong data '})
@api_view(['PUT'])
def update(request,id):
    updateobject=Product.objects.filter(id=id).first()
    if updateobject:
        serializedproduct=Productserlizer(instance=updateobject,data=request.data)
        if(serializedproduct.is_valid()):
            serializedproduct.save()
            return Response (data=serializedproduct.data)
            
    
    return Response({'msg':' product data not fount'})
@api_view(['DELETE'])
def delete(request,id):
    tr=Product.objects.filter(id=id).first()
    if(tr):
        Product.objects.filter(id=id).delete()
        return Response({'msg':'Product deleted'})
    

    return Response({'msg':' wrong data '})

    # try:
    #     obj = Product()
    #     obj.name = request.data['name']
    #     obj.details = request.data['details']
    #     obj.save()
        
    #     # Handle image field if present
    #     if 'image' in request.data:
    #         obj.image = request.data['image']
    #         # Process image upload or handle accordingly
        
    #     return Response({'msg': 'Data accepted'}, status=status.HTTP_201_CREATED)
    # except KeyError as e:
    #     return Response({'error': f'Missing key: {e}'}, status=status.HTTP_400_BAD_REQUEST)


    