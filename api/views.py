from django.shortcuts import render
import json
from rest_framework import status, generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer, Group, GroupSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ContactsView(APIView):
    """
    get:
    Return a list of all existing contacts 
    
    post:
    Create a new contact 
    
    put:
    Update a contact
    
    delete:
    Delete a contact
    """
    
    @swagger_auto_schema(
        responses={ status.HTTP_200_OK : ContactSerializer(many=True)}
    )
    
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
            
    @swagger_auto_schema(
        request_body=ContactSerializer,
        responses={
            status.HTTP_200_OK : ContactSerializer,
            status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
            }
        )
        
    def post(self, request):
            
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        response={status.HTTP_204_NO_CONTENT}
        )
        
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
      
    @swagger_auto_schema(
        responses={
        status.HTTP_200_OK : ContactSerializer,
        status.HTTP_400_BAD_REQUEST : openapi.Response(description="Missing information")
        }
    )   
        
      
    def put (self, request, contact_id):
        
         contact = Contact.objects.get(id=contact_id)
         contact.first_name = request.data.get("first_name")
         contact.last_name = request.data.get("last_name")
         contact.email = request.data.get("email")
         contact.phone = request.data.get("phone")
         contact.address = request.data.get("address")
         contact.save()
        
         serializer = ContactSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
class GroupView (generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
            
       
        
        
        