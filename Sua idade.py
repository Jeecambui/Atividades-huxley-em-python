ano_nasc = int(input("Qual o ano de Nascimento? "))
ano_atual = int(input("Qual o ano atual? "))

idade = ano_atual - ano_nasc

print("Sua idade é de", idade, "anos")

if(idade>=18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
