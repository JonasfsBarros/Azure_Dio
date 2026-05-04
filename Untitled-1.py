print("Digite a necessidade do time:")
necessidade = input()

if necessidade == "armazenar arquivos":
    print("Azure Blob Storage")
elif necessidade == "armazenar dados relacionais":
    print("Azure SQL Database")
elif necessidade == "executar codigo sob demanda":
    print("Azure Functions")
elif necessidade == "hospedar sistemas operacionais":
    print("Azure Virtual Machines")
else:
    print("Servico desconhecido")