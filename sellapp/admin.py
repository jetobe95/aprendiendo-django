from django.contrib import admin

from .models import *



class CuentaAdmin(admin.ModelAdmin):
  list_display = ['correo']



admin.site.register(Cuenta,CuentaAdmin)


class InlineCliente(admin.TabularInline):
  model = CuentaCliente

class ClienteAdmin(admin.ModelAdmin):
  inlines = [InlineCliente]


admin.site.register(Cliente,ClienteAdmin)

class CuentaClienteAdmin(admin.ModelAdmin):
  list_display = ['ciente']




class InlinePlanAdmin(admin.TabularInline):
  extra = 0
  model = PlanCuenta

class PlanAdmin(admin.ModelAdmin):
  inlines = [InlinePlanAdmin]


admin.site.register(Plan,PlanAdmin)
