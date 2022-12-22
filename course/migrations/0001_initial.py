# Generated by Django 4.1.2 on 2022-12-12 10:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('course_catagory_name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('course_name', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('course_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.coursecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]