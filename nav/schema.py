import graphene
from graphene_django import DjangoObjectType
from nav.models import *

class NavbarType(DjangoObjectType):
    class Meta:
        model = Navbar

# querys
class Query(graphene.ObjectType):

    # Navbar
    navbar = graphene.Field(NavbarType,
                              id=graphene.Int(),
                              user_id=graphene.Int())

    all_navbars = graphene.List(NavbarType)


    # Resolve object list 
     def resolve_all_navbars(self, info, **kwargs):
        return Navbar.objects.all()

   

    #  Resolve single objects
    def resolve_navbar(self, info, **kwargs):
        id = kwargs.get('id')
        project_id = kwargs.get('project_id')

        if id is not None:
            return Navbar.objects.get(pk=id)

        if project_id is not None:
            return Navbar.objects.get(project_id=project_id)


        return None





