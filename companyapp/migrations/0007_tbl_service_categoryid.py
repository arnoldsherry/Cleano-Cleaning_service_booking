# Generated migration to add categoryid field

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_delete_tbl_login'),
        ('companyapp', '0006_alter_tbl_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_service',
            name='categoryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tbl_category'),
        ),
    ]
