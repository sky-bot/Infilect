# Generated by Django 2.2.4 on 2020-05-10 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('group_id', models.CharField(db_column='GroupId', max_length=14, primary_key=True, serialize=False)),
                ('group_name', models.CharField(blank=True, db_column='GroupName', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('photo_id', models.IntegerField(db_column='PhotoId', primary_key=True, serialize=False)),
                ('owner_id', models.CharField(blank=True, db_column='OwnerId', max_length=10, null=True)),
                ('server', models.CharField(db_column='ServerId', max_length=10)),
                ('farm', models.IntegerField(blank=True, db_column='Farm', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=100, null=True)),
                ('is_public', models.BooleanField(db_column='IsPublic', default=False)),
                ('owner_name', models.CharField(blank=True, db_column='OwnerName', max_length=50, null=True)),
                ('date_added', models.DateTimeField(db_column='DateAdded')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authapp.Groups')),
            ],
        ),
    ]
