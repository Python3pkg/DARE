# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DefaultDareBigJobPilot'
        db.create_table('darewap_defaultdarebigjobpilot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(default='New', max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pilot_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('service_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('data_service_url', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('working_directory', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('cores_per_node', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('number_of_processes', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('queue', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('walltime', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal('darewap', ['DefaultDareBigJobPilot'])

        # Adding model 'DareBigJobTask'
        db.create_table('darewap_darebigjobtask', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(default='New', max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('dare_bigjob', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['darewap.DareBigJob'])),
            ('dare_bigjob_pilot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['darewap.DareBigJobPilot'], null=True, blank=True)),
            ('script', self.gf('django.db.models.fields.TextField')(default='def tasks(NUMBER_JOBS=1):\n    tasks = []\n    for i in range(NUMBER_JOBS):\n        compute_unit_description = {\n        "executable": "/bin/echo",\n        "arguments": ["Hello", "$ENV1", "$ENV2"],\n        "environment": [\'ENV1=env_arg1\', \'ENV2=env_arg2\'],\n        "number_of_processes": 4,\n        "spmd_variation": "mpi",\n        "output": "stdout.txt",\n        "error": "stderr.txt"}\n        tasks.append(compute_unit_description)\n    return tasks', blank=True)),
            ('inputfiles', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('outputfiles', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('darewap', ['DareBigJobTask'])

        # Adding model 'DareBigJobPilot'
        db.create_table('darewap_darebigjobpilot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(default='New', max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pilot_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('service_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('data_service_url', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('working_directory', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('cores_per_node', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('number_of_processes', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('queue', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('walltime', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('dare_bigjob', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['darewap.DareBigJob'])),
            ('time_started', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('darewap', ['DareBigJobPilot'])

        # Adding model 'DareBigJob'
        db.create_table('darewap_darebigjob', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='name', max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(default='New', max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('cordination_url', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('other_info', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('darewap', ['DareBigJob'])


    def backwards(self, orm):
        # Deleting model 'DefaultDareBigJobPilot'
        db.delete_table('darewap_defaultdarebigjobpilot')

        # Deleting model 'DareBigJobTask'
        db.delete_table('darewap_darebigjobtask')

        # Deleting model 'DareBigJobPilot'
        db.delete_table('darewap_darebigjobpilot')

        # Deleting model 'DareBigJob'
        db.delete_table('darewap_darebigjob')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'darewap.darebigjob': {
            'Meta': {'object_name': 'DareBigJob'},
            'cordination_url': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '30'}),
            'other_info': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'darewap.darebigjobpilot': {
            'Meta': {'object_name': 'DareBigJobPilot'},
            'cores_per_node': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dare_bigjob': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['darewap.DareBigJob']"}),
            'data_service_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '30'}),
            'number_of_processes': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'pilot_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'queue': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'service_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '30'}),
            'time_started': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'walltime': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'working_directory': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'darewap.darebigjobtask': {
            'Meta': {'object_name': 'DareBigJobTask'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dare_bigjob': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['darewap.DareBigJob']"}),
            'dare_bigjob_pilot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['darewap.DareBigJobPilot']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inputfiles': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '30'}),
            'outputfiles': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {'default': '\'def tasks(NUMBER_JOBS=1):\\n    tasks = []\\n    for i in range(NUMBER_JOBS):\\n        compute_unit_description = {\\n        "executable": "/bin/echo",\\n        "arguments": ["Hello", "$ENV1", "$ENV2"],\\n        "environment": [\\\'ENV1=env_arg1\\\', \\\'ENV2=env_arg2\\\'],\\n        "number_of_processes": 4,\\n        "spmd_variation": "mpi",\\n        "output": "stdout.txt",\\n        "error": "stderr.txt"}\\n        tasks.append(compute_unit_description)\\n    return tasks\'', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'darewap.defaultdarebigjobpilot': {
            'Meta': {'object_name': 'DefaultDareBigJobPilot'},
            'cores_per_node': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_service_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '30'}),
            'number_of_processes': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'pilot_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'queue': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'service_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'walltime': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'working_directory': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'darewap.job': {
            'Meta': {'object_name': 'Job'},
            'cordination_url': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_jobs'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'darewap.jobdetailedinfo': {
            'Meta': {'object_name': 'JobDetailedInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobinfo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_detailed_info'", 'null': 'True', 'to': "orm['darewap.JobInfo']"}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'darewap.jobinfo': {
            'Meta': {'object_name': 'JobInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'detail': ('picklefield.fields.PickledObjectField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_info'", 'null': 'True', 'to': "orm['darewap.Job']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'user_pilot': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobuserpilots'", 'null': 'True', 'to': "orm['darewap.UserPilots']"}),
            'user_task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobusertasks'", 'null': 'True', 'to': "orm['darewap.UserTasks']"})
        },
        'darewap.usercontext': {
            'Meta': {'object_name': 'UserContext'},
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'SSH'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_context'", 'null': 'True', 'to': "orm['auth.User']"}),
            'usercert': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'userkey': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'userpass': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'userproxy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'darewap.userpilots': {
            'Meta': {'object_name': 'UserPilots'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'detail': ('picklefield.fields.PickledObjectField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_pilots'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'darewap.userresource': {
            'Meta': {'object_name': 'UserResource'},
            'allocation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cores_per_node': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'data_service_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'processes_per_node': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'queue': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'service_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_resource'", 'null': 'True', 'to': "orm['auth.User']"}),
            'working_directory': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'darewap.usertasks': {
            'Meta': {'object_name': 'UserTasks'},
            'args': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'env': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'executable': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inputfiles': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'num_of_cores': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'num_of_processes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'num_of_tasks': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'outputfiles': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'script': ('django.db.models.fields.TextField', [], {'default': '\'def tasks(NUMBER_JOBS=1):\\n    tasks = []\\n    for i in range(NUMBER_JOBS):\\n        compute_unit_description = {\\n        "executable": "/bin/echo",\\n        "arguments": ["Hello", "$ENV1", "$ENV2"],\\n        "environment": [\\\'ENV1=env_arg1\\\', \\\'ENV2=env_arg2\\\'],\\n        "number_of_processes": 4,\\n        "spmd_variation": "mpi",\\n        "output": "stdout.txt",\\n        "error": "stderr.txt"}\\n        tasks.append(compute_unit_description)\\n    return tasks\'', 'blank': 'True'}),
            'spmd_variation': ('django.db.models.fields.CharField', [], {'default': "'single'", 'max_length': '30', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_tasks'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['darewap']