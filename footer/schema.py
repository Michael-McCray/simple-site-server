import graphene
from graphene_django import DjangoObjectType
from footer.models import *

class FooterType(DjangoObjectType):
    class Meta:
        model = Footer

# querys
class Query(graphene.ObjectType):

    # Footer
    footer = graphene.Field(FooterType,
                              id=graphene.Int(),
                              user_id=graphene.Int())

    all_footers = graphene.List(FooterType)


    # Resolve object list 
     def resolve_all_footers(self, info, **kwargs):
        return Footer.objects.all()

   

    #  Resolve single objects
    def resolve_footer(self, info, **kwargs):
        id = kwargs.get('id')
        project_id = kwargs.get('project_id')

        if id is not None:
            return Footer.objects.get(pk=id)

        if project_id is not None:
            return Footer.objects.get(project_id=project_id)


        return None





