# Generated by Django 2.2.1 on 2019-06-01 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dip_manager', '0005_auto_20190601_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic_comm',
            name='task',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='task_of_comm_of_pic', to='dip_manager.Task'),
            preserve_default=False,
        ),
    ]
