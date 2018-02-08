from django.db import models
from django.utils import timezone

# Create your models here.

##创建文章模型Post
'''
class Post(models.Model):- 这一行定义了我们的模型（这是一个object）。
class 是一个特殊的关键字，表示我们正在定义一个对象。
Post是我们模特的名字 我们可以给它一个不同的名字（但是我们必须避免特殊字符和空格）。
始终以大写字母开始课程名称。
models.Model 意味着Post是一个Django模型，所以Django知道它应该被保存在数据库中。
models.CharField - 这是如何定义有限数量字符的文本。
models.TextField - 这是一个没有限制的长文本。听起来非常适合博客文章内容，对吗？
models.DateTimeField - 这是一个日期和时间。
models.ForeignKey - 这是另一个模型的链接。
方法通常会 return 一些东西。 例如在 __str__ 方法中就有这个。 在这种情况下，当我们调用 __str__() 我们将得到文章
标题的文本 （字符串）。
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
