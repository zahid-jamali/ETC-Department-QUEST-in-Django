# Generated by Django 2.2.12 on 2022-07-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0012_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('text', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]