# Generated by Django 4.1 on 2022-12-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0022_alter_courses_course_desc_alter_faculty_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='text',
            field=models.TextField(),
        ),
    ]