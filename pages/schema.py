import graphene
from graphene_django import DjangoObjectType
from pages.models import *

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class PageType(DjangoObjectType):
    class Meta:
        model = Page

# querys
class Query(graphene.ObjectType):

    # pages
    page = graphene.Field(PageType,
                              id=graphene.Int(),
                              Project_id=graphene.Int(),
                              order=graphene.Int())

    all_pages = graphene.List(PageType)


    # projects
    project = graphene.Field(ProjectType,
                              id=graphene.Int(),
                              user_id=graphene.Int())

    all_projects = graphene.List(ProjectType)


    # Resolve object list 
    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_all_pages(self, info, **kwargs):
        project_id = kwargs.get('project_id')

        if project_id is not None:
            project = Project.objects.get(pk=project_id)
            return Page.objects.filter(project=project).all()

        return None

    #  Resolve single objects
    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Product.objects.get(pk=id)

        return None

    def resolve_page(self, info, **kwargs):
        id = kwargs.get('id')
        order = kwargs.get('order')

        if id is not None:
            return Page.objects.get(pk=id)

        if order is not None:
            return Page.objects.get(pk=id,order=order)

        return None




