import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	# For Admin
	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'
		
class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	autor_name = models.CharField('Имя автора', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 200)

	def __str__(self):
		return self.autor_name

	# For Admin
	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'