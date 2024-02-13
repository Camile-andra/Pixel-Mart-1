# Generated by Django 5.0.2 on 2024-02-10 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Variacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(blank=True, max_length=50, null=True)),
                ("preco", models.FloatField()),
                ("preco_promotional", models.FloatField(default=0)),
                ("estoque", models.PositiveIntegerField(default=1)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.produto",
                    ),
                ),
            ],
        ),
    ]
