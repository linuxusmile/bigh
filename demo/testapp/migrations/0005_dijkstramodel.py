# Generated by Django 2.0.3 on 2019-03-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DijkstraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg1', models.CharField(max_length=15)),
                ('reg2', models.CharField(max_length=15)),
                ('reg3', models.CharField(max_length=15)),
                ('reg4', models.CharField(max_length=15)),
                ('reg5', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'regional',
            },
        ),
    ]
