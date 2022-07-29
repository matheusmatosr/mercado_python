def recebeInf():
  l_compras = []
  continuar = 's'
  while continuar == 's':
    comprar = input('O que deseja comprar? ')
    l_compras.append(comprar)
    continuar = input('Deseja continuar comprando? ')
  return l_compras

def total(l_compras):
  valor = 0
  for i in range(len(l_compras)):
    if l_compras[i] == 'picanha':
      valor = valor + 90
    elif l_compras[i] ==  'pao de alho':
      valor = valor + 15  
    elif l_compras[i] == 'arroz':
      valor = valor + 25
    elif l_compras[i] == 'tropeiro':
      valor = valor + 40
    elif l_compras[i] == 'refrigerante':
      valor = valor + 10
    else:
      print('Produto indisponível')
  return valor

def desconto(valor):
  if valor >= 200:
    desconto = (valor*15) / 100
    valor_novo = valor - desconto
    print(f'Desconto de R${desconto}')
    print(f'Total a pagar com desconto R${valor_novo}')
    print(f'Total a pagar sem desconto R${valor}')
  else:
    print(f'Total a pagar R${valor}')

def main():
  r = recebeInf()
  t = total(r)
  d = desconto(t)

main()