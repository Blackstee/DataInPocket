# Generated by Django 2.2.1 on 2019-06-01 16:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dip_manager', '0003_auto_20190531_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pic_task',
            old_name='comment',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='change',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 19211, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 16864, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 16912, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 18073, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 13497, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 23, 8, 14614, tzinfo=utc), null=True),
        ),
    ]
