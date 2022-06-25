import graphene
from django.core.mail import EmailMessage
# users/schema.py
from graphene_django import DjangoObjectType
from users.models import *
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from numpy import random



# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class UserType(DjangoObjectType):
    class Meta:
        model = User

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile



# Add querys to object
class Query(graphene.ObjectType):

    # users
    user = graphene.Field(UserType,
                              user_id=graphene.String(),
                              email=graphene.String(),
                              username=graphene.String())

    all_users = graphene.List(UserType)


    # profiles
    profile = graphene.Field(ProfileType,
                              id=graphene.Int(),
                              user_id=graphene.String())

    all_profiles = graphene.List(ProfileType)

   

    # Resolve object list 
    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_profiles(self, info, **kwargs):
        return Profile.objects.all()


    #  Resolve single objects
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        email = kwargs.get('email')

        if id is not None:
            return User.objects.get(pk=id)

        if email is not None:
            return User.objects.get(email=email)

        return None

    def resolve_profile(self, info, **kwargs):
        id = kwargs.get('id')
       
        if user_id is not None:
            user = User.objects.get(pk=user_id)
            return Profile.objects.get(user=user)

        if id is not None:
            return Profile.objects.get(pk=id)
            
        return None

    
