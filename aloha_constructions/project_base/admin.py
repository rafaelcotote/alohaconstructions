from django.contrib import admin
from .models import CadastroProjeto, Task

class CadastroProjetoAdmin(admin.ModelAdmin):
    list_display = ['project_name']
    list_filter = ['project_name']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['text', 'completed', 'estimated_time']

admin.site.register(CadastroProjeto, CadastroProjetoAdmin)
admin.site.register(Task, TaskAdmin)