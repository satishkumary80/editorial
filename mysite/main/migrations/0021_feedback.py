# Generated by Django 2.2.1 on 2019-07-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_essay_essay_contributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_title', models.CharField(max_length=100)),
                ('feedback_date', models.DateTimeField(auto_now=True)),
                ('feedback_content', models.TextField(help_text='Share Your Ideas Here!')),
                ('feedback_user_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
