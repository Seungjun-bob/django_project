from django.db import models

# Create your models here.
class Question(models.Model):
    # 제목은 최대 200자로 제한된다. 제한된 텍스처 -> CharField
    subject = models.CharField(max_length=200)
    # 글자수를 제한 할 수 없는 텍스처 -> TextField
    content = models.TextField()
    create_date = models.DateTimeField()

    # id값 대신 제목을 표시할 수 있다.
    def __str__(self):
        return self.subject

class Answer(models.Model):
    # on_delete -> Question이 삭제되면 Answer 또한 같이 삭제 된다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

