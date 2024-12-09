def conversor_temperatura():
print("Conversor de Temperaturas")
print("-------------------------")

while True:  # Loop que permite múltiplas conversões
    # Escolha da escala de temperatura de origem
    print("Escolha a escala de temperatura de origem:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    print("0. Sair")
    origem = int(input("Digite o número da opção: "))

    if origem == 0:  # Opção para sair
        print("Saindo do conversor. Até logo!")
        break

    # Escolha da escala de temperatura de destino
    print("Escolha a escala de temperatura de destino:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    destino = int(input("Digite o número da opção: "))

    # Leitura do valor da temperatura
    temperatura = float(input("Digite o valor da temperatura: "))

    # Conversão da temperatura
    if origem == 1 and destino == 2:
        resultado = (temperatura * 9/5) + 32
    elif origem == 1 and destino == 3:
        resultado = temperatura + 273.15
    elif origem == 2 and destino == 1:
        resultado = (temperatura - 32) * 5/9
    elif origem == 2 and destino == 3:
        resultado = (temperatura - 32) * 5/9 + 273.15
    elif origem == 3 and destino == 1:
        resultado = temperatura - 273.15
    elif origem == 3 and destino == 2:
        resultado = (temperatura - 273.15) * 9/5 + 32

    # Impressão do resultado
    print(f"{temperatura} {['°C', '°F', 'K'][origem-1]} é igual a {resultado} {['°C', '°F', 'K'][destino-1]}")

    # Chamada da função
    conversor_temperatura()
