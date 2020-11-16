# Generated by Django 2.2 on 2020-11-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlyerDetail',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('client_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=20)),
                ('creators_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='image/pic')),
            ],
        ),
    ]
