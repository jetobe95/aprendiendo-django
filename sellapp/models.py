from django.db import models


class Cliente(models.Model):
  nombre_completo = models.CharField(max_length=200)
  celular = models.CharField(max_length=15)

  def __str__(self) -> str:
    return f'{self.nombre_completo}'

class Cuenta(models.Model):
  correo = models.EmailField()
  contrasena = models.CharField(max_length=200)
  es_maestra = models.BooleanField()

  def __str__(self) -> str:
    return f'{self.correo}'

class CuentaCliente(models.Model):
  ciente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)
  cuenta = models.ForeignKey(Cuenta,on_delete=models.DO_NOTHING)
  precio_mes = models.IntegerField()


class Plan(models.Model):
  tipo = models.CharField(max_length=200,choices=[('spotify','Spotify'),('Netflix','Netflix'),('Star plus','Star plus')])
  cuenta_maestra = models.OneToOneField(Cuenta,on_delete=models.CASCADE)
  precio = models.IntegerField()
  fecha_pago_recurrente = models.DateField()
  capacidad = models.IntegerField()

  

  def __str__(self) -> str:
    return f'[{self.tipo}] {self.cuenta_maestra.correo}'


class PlanCuenta(models.Model):
  cuenta = models.ForeignKey(Cuenta,on_delete=models.DO_NOTHING)
  plan = models.ForeignKey(Plan,on_delete=models.DO_NOTHING)
  renovacion_mensual = models.IntegerField('Renovación mensual. Ej cada 1 mes, 2 meses, etc')
  precio_mes = models.IntegerField()

class CobroPlanCuenta(models.Model):
  plan_cuenta = models.ForeignKey(PlanCuenta,on_delete=models.DO_NOTHING)
  periodo_pagado = models.DateField()
  fue_pagado = models.BooleanField()
  fecha_pago = models.DateField()

