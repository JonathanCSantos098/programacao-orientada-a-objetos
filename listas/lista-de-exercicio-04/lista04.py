with open ("amazon.csv") as arqui:

	quest_1=(0)
	quest_2=(0)
	quest_3=(0)
	quest_4=(0)

	for linha in arqui:
		dados = linha.strip("\n").split(",")
		num_queimadas = dados[3].replace(".","")

		if ((dados[1] == '"Acre"')  and (int(dados[0]) == 2015)):			
			quest_1+=int(num_queimadas)

		elif ((dados[1] == '"Ceara"') and (int(dados[0]) == 2014)):
			quest_2+=int(num_queimadas)

		elif (dados[1] == '"Amazonas"'):
			quest_3+=int(num_queimadas)

		if (dados[0] == '"year"'):
			continue

		elif ((int(dados[0])>=2010) and (dados[1] == '"Mato Grosso"')):
			quest_4+=int(num_queimadas)
		

print ("Em 2015 o Acre sofreu {} Queimadas".format(quest_1))
print ("Em 2014 o Ceará sofreu {} Queimadas".format(quest_2))
print ("Amazonas sofreu {} Queimadas".format(quest_3))
print ("Mato Grosso sofreu {} Queimadas".format(quest_4))