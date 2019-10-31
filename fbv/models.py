from django.db import models

# Create your models here.
class Todo(models.Model):

    # serializers - checked, title, due_date
    # 했는지 여부
    checked = models.BooleanField(
        default = False
    )
    # 작성시간
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    # 수정시간
    modified_at = models.DateTimeField(
        auto_now = True
    )
    # 제목
    title = models.CharField(
        max_length = 150
    )
    # 마감기한
    # 사용: date(1960, 8, 1)
    due_date = models.DateField()
    