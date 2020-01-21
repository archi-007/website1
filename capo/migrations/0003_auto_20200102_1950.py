# Generated by Django 3.0.1 on 2020-01-02 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capo', '0002_accessories_individualaccessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50)),
                ('app_price', models.IntegerField()),
                ('app_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='individualaccessories',
            name='iaccessories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capo.Accessories'),
        ),
        migrations.CreateModel(
            name='Individualapparel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_1', models.CharField(max_length=50)),
                ('feature_2', models.CharField(max_length=50)),
                ('feature_3', models.CharField(max_length=50)),
                ('iapparel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capo.Apparel')),
            ],
        ),
    ]
