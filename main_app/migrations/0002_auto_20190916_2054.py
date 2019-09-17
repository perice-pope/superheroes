# Generated by Django 2.2.5 on 2019-09-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='superhero',
            name='add_powers',
            field=models.ManyToManyField(to='main_app.Power'),
        ),
    ]