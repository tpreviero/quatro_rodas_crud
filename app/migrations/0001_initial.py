# Generated by Django 2.0.1 on 2018-01-20 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('madified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=128, verbose_name='Descrição do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Preço')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produto',
            field=models.ManyToManyField(to='app.Produto'),
        ),
    ]
