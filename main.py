from src.webscraping.spamBot import SpamBot

"""
    A primeira coisa a se fazer é chamar pela classe SpamBot. Essa classe contém um total de três métodos,
    o método de inicialização dessa classe exige dois parâmetros. O primeiro parâmetro é a pasta onde o 
    arquívo contendo o relatório de informações sobre os jogadores é criado. O segundo parâmetro é o nome
    do arquívo a ser criado.

    Chame o método getInformationAboutServers() para obter informações sobre a quantidade de servidores
    cadastrados disponíveis para o scrapping de dados.

    Você também pode chamar pelo método getServersList(typeS=None) que possuí um parâmetro default chamado
    typeS. Caso você altere o parâmetro default você receberá o nome dos servidores cadastrados como
    informação em seu terminal. Por padrão esse método retorna uma tabela de dados.

    O último e mais importante é o método getPlayersFromServer(name_of_server) que recebe o nome de um ser-
    vidor cadastrado. Caso você passe o nome de um servidor não existente o erro é informado, mas caso o nome
    conste dentro da lista de servidores, um JSON é criado contendo as informações dos jogadores do servidor.
"""

#  Inicia uma instância da classe SpamBot.
myBot = SpamBot("./logs", "playersBaiakIllusions")

#  Exibe informações sobre a quantidade de servidores cadastrados e disponíveis.
myBot.getInformationAboutServers()

#  Retorna um array de servidores cadastrados. 
myBot.getServersList()

#  Exibe informações formatadas sobre todos os servidores cadastrados na lista.
myBot.getServersList("print")

#  Gera um JSON dentro da pasta LOGS chamado TESTE do servidor Baiak Illusions.
myBot.getPlayersFromServer("Baiak Illusions")

#  Informa que o servidor não está cadastrado dentro da lista de servidores, portanto ele não existe.
myBot.getPlayersFromServer("Baiakão do Maurício")
