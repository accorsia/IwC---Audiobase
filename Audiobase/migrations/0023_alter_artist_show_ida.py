# Generated by Django 4.2.1 on 2023-06-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Audiobase', '0022_alter_artist_show_ida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='show_ida',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Ida'),
        ),
    ]
