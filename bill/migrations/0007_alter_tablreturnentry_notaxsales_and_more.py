# Generated by Django 4.0.6 on 2023-07-05 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_alter_bill_discount_amount_alter_bill_grand_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablreturnentry',
            name='NoTaxSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tablreturnentry',
            name='ZeroTaxSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tablreturnentry',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tablreturnentry',
            name='tax_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tablreturnentry',
            name='taxable_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tblsalesentry',
            name='NoTaxSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tblsalesentry',
            name='ZeroTaxSales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tblsalesentry',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tblsalesentry',
            name='tax_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tblsalesentry',
            name='taxable_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tbltaxentry',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tbltaxentry',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tbltaxentry',
            name='tax_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tbltaxentry',
            name='taxable_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tbltaxentry',
            name='vat_refund_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
