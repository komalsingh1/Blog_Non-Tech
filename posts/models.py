from django.db import models

# Create your models here.
class Post(models.Model):
	title=models.charField(max_length=120)
	content=models.TextField()
	updated=modelss.DateTimeField(auto_now='True',auto_now_add='False')
	timestamp=modelss.DateTimeField(auto_now='False',auto_now_add='True')

	def _str_(self):
	 return self.title
