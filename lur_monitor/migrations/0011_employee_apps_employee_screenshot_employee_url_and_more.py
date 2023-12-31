# Generated by Django 4.2.5 on 2023-12-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lur_monitor', '0010_alter_empid_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='apps',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='employee',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eEmail',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ePhone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
