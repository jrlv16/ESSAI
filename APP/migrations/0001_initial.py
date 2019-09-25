# Generated by Django 2.1.7 on 2019-09-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom du client')),
                ('email', models.CharField(max_length=50, verbose_name='Addresse mail')),
                ('numerofact', models.PositiveSmallIntegerField(unique=True, verbose_name='Numéro de Facture')),
            ],
        ),
    ]
