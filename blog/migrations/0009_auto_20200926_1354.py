# Generated by Django 3.0.6 on 2020-09-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200926_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_filed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='singlepost',
            name='video_categories',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
