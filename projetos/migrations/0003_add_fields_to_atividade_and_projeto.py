from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_projeto_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
        ),
        migrations.AddField(
            model_name='atividade',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='responsaveis',
            field=models.ManyToManyField(related_name='projetos_responsavel', to='auth.user'),
        ),
    ]
