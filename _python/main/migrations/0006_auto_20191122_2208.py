# Generated by Django 2.2.4 on 2019-11-22 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191120_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentannotation',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='main.Resource'),
        ),
        migrations.AlterField(
            model_name='contentcollaborator',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.ContentNode'),
        ),
        migrations.AlterField(
            model_name='contentnode',
            name='casebook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contents', to='main.Casebook'),
        ),
        migrations.AlterField(
            model_name='unpublishedrevision',
            name='annotation',
            field=models.ForeignKey(blank=True, db_constraint=False, db_index=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.ContentAnnotation'),
        ),
        migrations.AlterField(
            model_name='unpublishedrevision',
            name='casebook',
            field=models.ForeignKey(blank=True, db_constraint=False, db_index=False, help_text='The draft casebook.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='casebook_revisions', to='main.Casebook'),
        ),
        migrations.AlterField(
            model_name='unpublishedrevision',
            name='node',
            field=models.ForeignKey(blank=True, db_constraint=False, db_index=False, help_text='Node in the draft.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='revisions', to='main.ContentNode'),
        ),
        migrations.AlterField(
            model_name='unpublishedrevision',
            name='node_parent',
            field=models.ForeignKey(blank=True, db_constraint=False, db_index=False, help_text='Corresponding node in the original, published casebook.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='draft_revisions', to='main.ContentNode'),
        ),
    ]
