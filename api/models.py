from django.db import models

class Employee(models.Model):
    full_name = models.CharField('ФИО', max_length=255)
    passport_data = models.TextField('Паспортные Данные')
    passport_photo = models.ImageField(upload_to='passport_photos/')
    hours_worked = models.FloatField('Отработаннные часы работы')
    total_hours_worked = models.FloatField('Полные часы работы')
    deductions = models.FloatField('Удержание с ЗП')
    total_earnings = models.FloatField('Совокупный Заработок')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Profitability(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='profitability')
    client_payment = models.FloatField('Оплата клиента')
    employee_salary = models.FloatField('Зарплата клиента')
    accommodation_payment = models.FloatField('Оплата проживания')
    food_payment = models.FloatField('Оплата питания')
    transport_payment = models.FloatField('Оплата транспорта')
    agency_payment = models.FloatField('Оплата агенствам')
    total_profitability = models.FloatField('Общая прибыль')
    additional_expenses = models.FloatField('Дополнительные расходы')
    fines = models.FloatField('Штрафы')

    def __str__(self):
        return f'Рентабельность {self.employee.full_name}'
    
    class Meta:
        verbose_name = 'Рентабельность'
        verbose_name_plural = 'Рентабельность'
