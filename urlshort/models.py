from django.db import models
from hashlib import sha256 
from django.core.validators import URLValidator 
from django.core.exceptions import ValidationError
from graphql import GraphQLError 
# Create your models here.



class Url(models.Model):
	full = models.URLField(unique=True)
	hashed_full = models.URLField(unique=True)
	click_times = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)


	# Now let us count the click times and actually use the hash stuff 
	def clicking(self):
		self.click_times += 1
		self.save()



	def save(self,*args,**kwargs):
		if not self.id:
			# we would like to have the hexdigested hash to 8 chars. 
			# we don't need to overcomplicate this crap

			self.hashed_full = sha256(self.full.encode()).hexdigest()[:8]
		

		validation = URLValidator()
		try:
			validation(self.full)

		except ValidationError as error:
			raise GraphQLError('دوتس عزیز لطفا لینک درست رو قرار بده!!!')
		
		return super().save(*args, **kwargs)

