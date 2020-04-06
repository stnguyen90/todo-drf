# Generated by Django 3.0.5 on 2020-04-06 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TaskList')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.Task')),
                ('task_list', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TaskList')),
            ],
        ),
    ]
