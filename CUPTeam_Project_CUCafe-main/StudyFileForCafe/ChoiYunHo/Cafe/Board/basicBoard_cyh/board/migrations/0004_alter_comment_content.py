# Generated by Django 4.1 on 2023-01-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_remove_post_comment_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=None, null=True),
        ),
    ]
