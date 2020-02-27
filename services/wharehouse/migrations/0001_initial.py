# Generated by Django 2.2.7 on 2020-01-28 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('micromarket', '0001_initial'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('I', 'Insumo'), ('C', 'Combustível'), ('T', 'Transporte'), ('M', 'Material de Escritório'), ('TI', 'Técnico de Informática'), ('F', 'Funcionário')], max_length=2, verbose_name='Tipo de conta')),
                ('operation', models.CharField(choices=[('A', 'Aporte'), ('G', 'Gasto')], max_length=1, verbose_name='Tipo de operação')),
                ('value', models.FloatField(default=0, verbose_name='Valor')),
                ('receipt', models.TextField(blank=True, null=True, verbose_name='Foto do recibo (em base64)')),
                ('description', models.CharField(max_length=255, verbose_name='Observação')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Conta a pagar',
                'verbose_name_plural': 'Contas a pagar',
            },
        ),
        migrations.CreateModel(
            name='CapexType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Tipo de Capex')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizadem')),
            ],
            options={
                'verbose_name': 'Tipo de Capex',
                'verbose_name_plural': 'Tipos de Capex',
            },
        ),
        migrations.CreateModel(
            name='Expiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Data de validade')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Validade e lote',
                'verbose_name_plural': 'Validades e lotes',
            },
        ),
        migrations.CreateModel(
            name='PlanogramProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Preço do produto')),
                ('pair', models.IntegerField(verbose_name='Número de par')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Produto de Planograma',
                'verbose_name_plural': 'Produtos de Planograma',
            },
        ),
        migrations.CreateModel(
            name='PlanogramProductDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(verbose_name='Desconto em (%)')),
                ('begin', models.DateTimeField(verbose_name='Data e hora inicial')),
                ('end', models.DateTimeField(verbose_name='Data e hora final')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Desconto de itens do Planograma',
                'verbose_name_plural': 'Descontos de itens dos Planogramas',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=120, verbose_name='Nome do cliente')),
                ('token', models.CharField(max_length=255, verbose_name='Token da venda')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('products', models.ManyToManyField(to='wharehouse.PlanogramProduct', verbose_name='Produtos vendidos')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição do produto')),
                ('image', models.TextField(blank=True, null=True, verbose_name='Imagem em base64')),
                ('barcode', models.CharField(max_length=32, verbose_name='Código de barras')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantidade em estoque')),
                ('isActive', models.BooleanField(blank=True, default=True, null=True, verbose_name='Produto ativo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('expiration', models.ManyToManyField(blank=True, to='wharehouse.Expiration', verbose_name='Datas de validade e lotes')),
                ('invoices', models.ManyToManyField(blank=True, to='invoice.Invoice', verbose_name='Notas que deram baixa neste produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.AddField(
            model_name='planogramproduct',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wharehouse.PlanogramProductDiscount', verbose_name='Desconto no item do planograma'),
        ),
        migrations.AddField(
            model_name='planogramproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wharehouse.Product', verbose_name='Produto da Nota Fiscal'),
        ),
        migrations.CreateModel(
            name='Planogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=8, verbose_name='Versão do Planograma')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('products', models.ManyToManyField(to='wharehouse.PlanogramProduct', verbose_name='Produtos do Planograma')),
            ],
            options={
                'verbose_name': 'Planograma',
                'verbose_name_plural': 'Planogramas',
            },
        ),
        migrations.CreateModel(
            name='PicklistProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wharehouse.Product')),
            ],
            options={
                'verbose_name': 'Produto de Picklist',
                'verbose_name_plural': 'Produtos de Picklist',
            },
        ),
        migrations.CreateModel(
            name='Picklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='Versão da Picklist')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('instalation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='micromarket.Instalation', verbose_name='Instalação')),
                ('products', models.ManyToManyField(to='wharehouse.PicklistProduct')),
            ],
            options={
                'verbose_name': 'Picklist',
                'verbose_name_plural': 'Picklists',
            },
        ),
        migrations.CreateModel(
            name='Capex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.TextField(verbose_name='QR Code em base64')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wharehouse.CapexType', verbose_name='Tipo de Capex')),
            ],
            options={
                'verbose_name': 'Capex',
                'verbose_name_plural': 'Capex',
            },
        ),
    ]