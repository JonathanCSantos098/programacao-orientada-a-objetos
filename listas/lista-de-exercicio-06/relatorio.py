with open ("usuarios.txt") as arquivo:
    with open ("relatorio.txt", "w") as arqui:
        for x in arquivo:
            print("___________________________________________________________________________\n",
            "ACME Inc.            Uso do espaço em disco pelos usuários\n",
            "N°.      Usuário     Espaço Utilizado        % do uso\n","         ",x.replace(",","\n"), file=arqui)