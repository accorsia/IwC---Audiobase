# Generated by Django 4.2.1 on 2023-06-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Audiobase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='bname',
            field=models.CharField(max_length=100, verbose_name='Album name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='gold',
            field=models.BooleanField(verbose_name='Gold record'),
        ),
        migrations.AlterField(
            model_name='album',
            name='plat',
            field=models.BooleanField(verbose_name='Platinum record'),
        ),
        migrations.AlterField(
            model_name='album',
            name='year',
            field=models.DateField(verbose_name='Release year'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='aname',
            field=models.CharField(max_length=100, verbose_name='Artist name'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='n_gold',
            field=models.IntegerField(default=0, verbose_name='Num. of gold records'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='n_plat',
            field=models.IntegerField(default=0, verbose_name='Num. of platinum records'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='nation',
            field=models.CharField(max_length=100, verbose_name='Nationality'),
        ),
    ]
