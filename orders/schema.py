import graphene
from graphene_django import DjangoObjectType
from orders.models import *
from products.models import *

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

# querys
class Query(graphene.ObjectType):

    # orders
    order = graphene.Field(OrderType,
                              id=graphene.Int(),
                              product_id=graphene.Int(),
                              email=graphene.String())

    all_orders = graphene.List(OrderType)


    # Resolve object list 
    def resolve_all_orders(self, info, **kwargs):
        product_id = kwargs.get('product_id')

        if product_id is not None:
            product = Product.objects.get(pk=product_id)
            return Order.objects.filter(product=product).all()

        return Order.objects.filter(product=product).all()


    #  Resolve single objects
    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        product_id = kwargs.get('product_id')
        email = kwargs.get('email')


        if id is not None:
            return Order.objects.get(pk=id)

        if product_id is not None:
            product = Product.objects.get(pk=product_id)
            return Order.objects.get(product=product)

        if email is not None:
            return Order.objects.get(email=email)


        return None


# Mutations 
class OrderMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.String(required=True)
        product_id = graphene.String(required=True)
        price = graphene.Int(required=True)
        address = graphene.String(required=True)
        email = graphene.String(required=True)
        
        
    # The class attributes define the response of the mutation
    order = graphene.Field(OrderType)


    def mutate( self,info,user_id,product_id,price,address,email):
        order = Order( user_id=user_id,product_id=product_id,price=price,address=address,email=email)
        order.save()

        # Notice we return an instance of this mutation
        return OrderMutation(order=order)

class UpdateOrderMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        delivered = graphene.Boolean(required=True)
        refund = graphene.Boolean(required=True)

    # The class attributes define the response of the mutation
    order = graphene.Field(OrderType)


    def mutate( self,info,id,delivered,refund):
        order = Order.objects.get(pk=id)

        if refund is not None:
            order.refund = refund
            order.save()

        if delivered is not None:
            order.delivered = delivered
            order.save()

        # Notice we return an instance of this mutation
        return UpdateOrderMutation(order=order)


# Add mutations to object
class Mutation(graphene.ObjectType):
    create_order = OrderMutation.Field()
    update_order = UpdateOrderMutation.Field()
    