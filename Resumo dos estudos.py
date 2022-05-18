#int #=números inteiro
#float #=números reais
#bool #=lógico/booleano
#str #=string/conjunto de caracteres
#type #=identifica o tipo do valor armazenado em uma variável

#Máscara de formatação
#%d ou %i #Exibe um valor inteiro
#%f #Exibe um valor decimal
#%Id #Exibe um número inteiro longo
#%e ou %E #Exibe um número exponencial (número científico)
#%c #Exibe um caractere
#%o #Exibe um número inteiro em formato octal
#%x ou %X #Exibe um número no formato hexadecimal
#%s #Exibe uma cadeia de caractere
#%r #Exibe true ou false

#input é a forma de interagir com o usuário, fazer com que ele insira algum dado
#essa função armazena dados do tipo string
#ou seja, se quiser fazer a entrada de números, deverá ser convertido o dado que foi coletado

#SEQUÊNCIA DE ESCAPES
    #\n => insere uma quebra de linha
    #\t => insere tabulação horizontal
    #\v => insere tabulação vertical
    #\r => Equivalente ao efeito da tecla Enter
    #\' => Aspas simples
    #\" => Aspas duplas
    #\\ => Insere uma barra invertida
    #\a => Chamado de ASC bell ou beep do sistema. Se houver suporte, aciona um bipe
    #\b => Aciona o backspace, ou seja, apaga o caractere anterior
    #\f => Insere uma quebra de página
    #\u => Insere uma caratere UNICODE. Deve acompanhar um código com 4 números

#ESTRUTURAS LÓGICAS
    #Operações
        # + adição
        # - subtração
        # * multiplicação
        # / divisão real
        # // divisão inteiro
        # ** Exponenciação
        # % resto da divisão

        # == igual a
        # != diferente de
        # > ou < maior ou menor que
        # >= ou <= maior igual ou menor igual

        # and = E
        # or = ou
        # not = não

    #IDENTAÇÃO
        # é uma forma de arrumar o código, fazendo
        #com que algumas linhas fiquem mais à direita
        #que outras, à medida que adicionamos espaços em seu início.

#Exemplo de Identação

idade = int(input('Digite a idade da pessoa: '))

if idade >= 18:
    print('maior idade')
else:
    print('menor idade')

    #ESTRUTURA DE DECISÃO
        #sua finalidade é comparar e efetuar um desvio de processamento
        #se a condição for verdadeira, as instruções determinadas após o if serã executadas

    #if, elif e else
        #elif é usado quando temos mais de uma condição e queremos
        #que ela seja executada antes do else

    #ESTRUTURA DE REPETIÇÃO
        #for é usado quando sabemos quantas vezes o laço deverá ser executado
        #while executa enquanto a condição verificada no início permanece verdadeira.
            #Usamos-o para dizer até quando ou em que condição um programa deve ser executado.

#FUNÇÕES
    #A declaração de uma função é dividida em três partes:
        #nome, parâmetros e corpo.
#Exemplo
    # def nome_da_função (parâmetros):
        #<instruções>
    # return "valor do retorno"

    #DEF é a palavra que determina o início da função.
    #PARÂMETROS: são informações que a função pode receber para o seu processamento.
        #Eles podem existir ou não.
    #CORPO DA FUNÇÃO: é o local em que é aplicada a sequência de instruções, como
        #entrada, processamento e/ou saída.
    #RETURN: Deve ser utilizado quando houver necessidade de retornar alguma informação
        #para a ação da função.
    #INDENTAÇÃO: Deve possuir quatro espaços em branco e pular duas linhas para o próximo
        #bloco de instruções (próxima função ou programação principal)

#ARQUIVO SEQUECIAL
    #arquivo sequencial é quand a leitura tem de ser feita de forma sequencial, ou seja, do inicio ao fim do arquivo
    #Para isso utilizamos algumas funções:

    #open() é utilizada para a abertura dos arquivos, sendo sua sintaxe:
    #arquivo = open('arquivo.txt','w')
        #essa variavel que contém dois parâmetros, contém primeiro o nome do arquivo e, depois, o modo como estamos
            #abrindo esse arquivo.
        #no caso do parâmetro 'w', ele é usado para fazer a escrita em um arquivo.
            #se utilizarmos ele em um arquivo já existente, ele reescreverá todo o conteúdo do arquivo, fazendo com que
                #todos os dados que estavam nele sejam apagados.

    #write() é utilizada para gravar informações em um arquivo exitente, sendo sua sintaxe:
    #arquivo.write('Curso Python n')
    #arquivo.write('Aula Prática')

    #close() é usado para encerrar o arquivo após a sua utilização.
        #ATENÇÃO: nunca abra o arquivo e depois o faça de novo sem antes fechar a instância.
        #arquivo.close()

    #read() é usado para realizar a leitura de todo conteúdo do arquivo, sendo a sintaxe:
        #leitura=open('arquivo.txt, 'r')
            #print leitura.read()
            # leitura.close()

    #FORMAS DE LEITURA/INTERAÇÃO COM ARQUIVOS DE TEXTO
        #r = abre o arquivo somente para leitura. E o arquivo já deve existir.

        #r+ = abre o arquivo para leitura e escrita. O arquivo deve já existir. A escrita começa
                #a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão
                #reescritas, conforme formos escrevendo.

        #w = abre o arquivo somente para escrita, no início do arquivo. Apagará o conteúdo do arquivo
                #se ele já existir. Criará um arquivo novo se não existir.

        #w+ = abre o arquivo para escrite e leitura, apagando o conteúdo preexistente.

        #a = abre o arquivo para escrita no final do arquivo. Não apaga o conteúdo preexistente.

        #a+ = abre o arquivo para escrita no final do arquivo e leitura.
