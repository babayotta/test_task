# Generated by Django 3.0.2 on 2020-01-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_text', models.CharField(max_length=200)),
                ('interval', models.FloatField()),
                ('step', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='dashboard/images/')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
