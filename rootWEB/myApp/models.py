from django.db import models
from django.utils import timezone

# Create your models here.

class user_tbl(models.Model) :
    user_id     = models.CharField(primary_key=True, max_length=50)
    user_pwd   = models.CharField(max_length=50)

class board_tbl(models.Model) :
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(user_tbl,
                               on_delete=models.CASCADE,
                               db_column='writer',
                               null=False
                               )
    content = models.TextField()
    regdate = models.DateTimeField(default=timezone.now)