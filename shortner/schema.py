import graphene 
from graphene_django.debug import DjangoDebug

import urlshort.schema 


class Query(urlshort.schema.Query, graphene.ObjectType):
	
	debug = graphene.Field(DjangoDebug, name='_debug')


class Mutation(urlshort.schema.Mutation, graphene.ObjectType):
	pass


schema = graphene.Schema(query=Query,mutation=Mutation)