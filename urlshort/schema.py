import graphene 
from graphene_django import DjangoObjectType
from .models import Url 
from django.db.models import Q 

class UrlType(DjangoObjectType):
	class Meta:
		model = Url
		fields = '__all__'


class Query(graphene.ObjectType):
	urls = graphene.List(UrlType, url=graphene.String(), first=graphene.Int(), skip=graphene.Int(), **kwargs)



	def resolve_urls(self, info, url=None, first=None, skip=None, *args,**kwargs):
		qs = Url.objects.all()

		if url:
			filterer = Q(full__icontains=url)
			qs = qs.filter(filterer) 
		
		
		if first:
			qs = qs[:first]

		if skip:
			qs = qs[skip:]

		return qs




# A mutation to make the URLs straight from Graphql 

class CreateUrl(graphene.Mutation):
	url = graphene.Field(UrlType)

	class Arguments:
		full = graphene.String()


	def mutate(self, info, full):
		url = Url(full=full)
		url.save()
		CreateUrl(url=url)


class Mutation(graphene.ObjectType):
	create_url = CreateUrl.Field()
