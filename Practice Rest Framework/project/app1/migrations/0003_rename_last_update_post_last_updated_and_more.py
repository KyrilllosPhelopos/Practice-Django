# Generated by Django 4.2.5 on 2023-09-26 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_category_post_custom_id_post_last_update_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_update',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish_data',
            new_name='publish_date',
        ),
    ]
