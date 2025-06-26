
from django.db import migrations
class Migration(migrations.Migration):
    
    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospede',
            old_name='cpf',
            new_name='CPF',
        ),
    ]
