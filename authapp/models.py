from django.db import models

# Create your models here.


class Groups(models.Model):
    group_id = models.CharField(db_column='GroupId', max_length=14, primary_key=True)
    group_name = models.CharField(db_column='GroupName', max_length=10, null=True, blank=True)
    description = models.CharField(db_column='Description', max_length=100, null=True, blank=True)
    rules = models.CharField(db_column="Rules", max_length=400, null=True, blank=True)
    members = models.IntegerField(db_column="Member", null=True, blank=True)
    pool_count = models.IntegerField(db_column="PoolCount", null=True, blank=True)

    def __int__(self):
        return self.group_id


class Photos(models.Model):
    photo_id = models.IntegerField(db_column='PhotoId', primary_key=True)
    owner_id = models.CharField(db_column='OwnerId', max_length=10, null=True, blank=True)
    server = models.CharField(db_column='ServerId', max_length=10)
    farm = models.IntegerField(db_column='Farm', null=True, blank=True)
    title = models.CharField(db_column='Title', max_length=100, null=True, blank=True)
    is_public = models.BooleanField(db_column='IsPublic', default=False)
    owner_name = models.CharField(db_column='OwnerName', max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(db_column="DateAdded")
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    def __int__(self):
        return self.photo_id


