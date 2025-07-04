from datetime import date

def calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento):
  """Calcula a idade de uma pessoa a partir da data de nascimento.

  Args:
    ano_nascimento: O ano de nascimento.
    mes_nascimento: O mês de nascimento.
    dia_nascimento: O dia de nascimento.

  Returns:
    A idade da pessoa em anos.
  """
  data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
  data_atual = date.today()
  idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
  return idade

# Solicita a data de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento: "))
dia_nascimento = int(input("Digite o dia de nascimento: "))

# Calcula e imprime a idade
idade = calcular_idade(ano_nascimento, mes_nascimento, dia_nascimento)
print(f"A idade da pessoa é: {idade} anos")
