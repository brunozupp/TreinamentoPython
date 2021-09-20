if __name__ == '__main__':

    times = ("Atlético-MG","Palmeiras","Flamengo","Fortaleza","Bragantino",
             "Corinthians","Internacional","Fluminense","Atletico-PR","Cuiabá",
             "Atlético-GO","São Paulo","Ceará SC","Santos","Bahia",
             "Juventude","Grêmio","América-MG","Sport Recife","Chapecoense")

    # A)
    print(f"5 primeiros colocados = {times[:5]}")

    # B)
    print(f"Os 4 últimos times da tabela são: {times[-4:]}")

    # C)
    print(f"Ordem alfabética: {sorted(times)}")

    # D)
    print(f"Chapecoense está na posição {times.index('Chapecoense') + 1} na tabela")