from validate_docbr import CPF
import re


def valida_cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def valida_nome(nombre):
    return nombre.isalpha()


def valida_rg(numero_rg):
    return len(numero_rg) == 9

def valida_celular(numero_celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta