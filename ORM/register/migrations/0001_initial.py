# Generated by Django 5.1 on 2024-09-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
