from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.hashers import *

def valida_cedula(value):
    sumador, decena_proxima, verificador,numero2=0,0,0,0
    cedula_str = str(value).replace("-","").replace(" ","")
    if len(cedula_str) != 11 or cedula_str == '0000000000':
        raise ValidationError((f'{value} No es una cedula valida'))
    else:
        digito_verificador = int(cedula_str[-1])
        for i in range(1,10,2):
            numero2 = int(cedula_str[i])*2
            if numero2 > 10:
                sumador+= (numero2 - 10) + 1
            else:
                sumador += numero2
                
        for i in range(0,10,2):
            sumador += int(cedula_str[i])

        decena_proxima = (int(str(sumador)[0])+1) * 10
        verificador = decena_proxima - sumador

        if verificador != digito_verificador: 
            raise ValidationError((f'{value} No es una cedula valida'))
        else:
            return value
