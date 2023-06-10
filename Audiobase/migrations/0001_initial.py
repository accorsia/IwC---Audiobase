# Generated by Django 4.2.1 on 2023-06-03 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('idb', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(default='bname_default', max_length=100)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('gold', models.BooleanField()),
                ('plat', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('ida', models.AutoField(primary_key=True, serialize=False)),
                ('aname', models.CharField(max_length=100)),
                ('stagename', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('age', models.IntegerField(default=0)),
                ('n_gold', models.IntegerField(default=0)),
                ('n_plat', models.IntegerField(default=0)),
                ('nation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(default='name_default', max_length=100)),
                ('pubdate', models.DateTimeField(verbose_name='date published')),
                ('length', models.IntegerField()),
                ('spoty_str', models.IntegerField()),
                ('ida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Audiobase.artist')),
                ('idb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Audiobase.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='ida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Audiobase.artist'),
        ),
    ]
