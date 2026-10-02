# Sumilador de compra de supermercado 

produto = "Arroz" 
preco_unitario = 5.79 
quantidade = 3 

# Cálculo do valor total 
valor_total = preco_unitario * quantidade 
# print(f'Valor total antes do desconto: {valor_total}')

#Aplicando desconto de 10% se a quantidade for maior que 2 
if quantidade > 2: 
    valor_total = valor_total * 0.9 
# print(f'Valor total depois do desconto: {valor_total:.2f}')

print("Produto:", produto) 
print("Quantidade comprada:", quantidade) 
print("Valor total da compra: R$", f"{valor_total:.2f}")
