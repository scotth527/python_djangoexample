from rest_framework import serializers
from django.db import models

# Create your models here. 

class Group(models.Model):
    group_name = models.CharField(default="", max_length=50)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(default="joke@aol.com", max_length=50)
    phone = models.CharField(default="3051234567", max_length=50)
    address = models.CharField(default="here", max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # group = models.ForeignKey(Group, related_name='contacts', on_delete=models.CASCADE) Look up the parameters for foreign key 
    

    

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()
        
class GroupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Group 
        exclude = ()
        
