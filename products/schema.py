import graphene
from graphene_django import DjangoObjectType
from products.models import *

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

# querys
class Query(graphene.ObjectType):

    # products
    product = graphene.Field(ProductType,
                              id=graphene.Int(),
                              project_id=graphene.Int())

    all_products = graphene.List(ProductType)


    # Resolve object list 
    def resolve_all_products(self, info, **kwargs):
        project_id = kwargs.get('project')

        if project_id is not None:
            project = Project.objects.get(pk=project_id)
            return Product.objects.filter(project=project).all()

        return None


    #  Resolve single objects
    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')


        if id is not None:
            return Product.objects.get(pk=id)


        return None

