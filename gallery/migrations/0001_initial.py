# Generated by Django 2.2.6 on 2019-10-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='无标题', max_length=50)),
                ('image', models.ImageField(default='default.png', upload_to='image/')),
                ('desc', models.CharField(default='作品简介', max_length=100)),
            ],
        ),
    ]
