import graphene
import pages.schema
import users.schema
import products.schema
import orders.schema



class Query(
   
    pages.schema.Query,
    users.schema.Query,
    products.schema.Query,
    orders.schema.Query,# Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    
    orders.schema.Mutation,
    # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)