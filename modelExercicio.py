
class modelExercicio:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.vetor  = [] #Está variável é um Array

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def exercicio01(self):
        aux = self.getA()
        self.setA(self.getB())
        self.setB(aux)
        return "Os valor de A é: {}, o valor de B é: {}".format(self.getA(),self.getB())

    def exercicio02(self, num1):
        return num1 -1

    def exercicio03(self, base, altura):
        return base * altura


    def exercicio04(self):
        diasAnos = 365
        diasMes = 30


        print("Escreva sua idade: ")
        ano = int(input())
        while ano < 0:
            if ano < 0:
                print("Idade Incorreta!")
                print("Escreva sua idade: ")
                ano = int(input())

        print("Escreva quantos meses: ")
        mes = int(input())
        while mes < 0:
            if mes < 0:
                print("Mês Incorreto!")
                print("Escreva quantos meses: ")
                mes = int(input())


        print("Escreva os dias: ")
        dia = int(input())
        while dia < 0:
            if dia < 0:
                print("Dia Incorreto!")
                print("Escreva os dias: ")
                dia = int(input())




        dia += (ano * diasAnos) + (mes * diasMes)


        print("A sua idade expressa em dias é de: {}".format(dia))



    def exercicio05(self, eleitores, vvalidos, vbrancos, vnulos  ):

        vvalidos = vvalidos * 100 / eleitores
        vbrancos = vbrancos * 100 / eleitores
        vnulos = vnulos * 100 / eleitores

        return " O total de votos válidos é: {} % \n O total de votos brancos é: {} % \n O total de votos nulos é :  {} % ".format(vvalidos, vbrancos, vnulos)

    def exercicio06(self, salario, reajuste):
        return (salario * reajuste / 100) + salario

    def exercicio07(self, num):
        if num < 0:
            return "\nNumero invalido"
        else:
            return num + (num * 0.28) + (num * 0.45)

    def exercicio08(self, nota1, nota2, nota3):
        return (nota1 + nota2 + nota3) / 3

    def exercicio09(self, macas):
        if macas < 12:
           return macas * 1.30
        else:
            return macas

    #exercício 10
    def preencherVetor(self, num):
        self.vetor.append(num) #Incluindo dados no vetor

    def visualizarVetor(self):
        for i in range(len(self.vetor)):
            print("{}º número: {}\n".format(i+1,self.vetor[i]))

    def ordenar(self):
        self.vetor.sort(reverse=True)
        self.visualizarVetor()

    def excluir(self, posicao):
        self.vetor.pop(posicao)
        self.visualizarVetor()

    def incluir(self, posicao, num):
        self.vetor[posicao].append(num)

    def exercicio14(self, final):
        resultado = ""
        for i in range(1,int(final)+1,1):
            resultado = resultado + "\n{}".format(i)
        return resultado

    def exercicio18(self, quantidade):
        soma = 0
        media = 0
        maior = 0
        for i in range(int(quantidade)):
            print("Informe o {}º número: ".format(i+1))
            num = int(input())
            soma = soma + num #Preparando a soma para a média

            if i == 0:
                maior = num
            else:
                if num > maior:
                    maior = num

        media = soma / quantidade
        print("A média dos valores digitados é: {}\nO maior número digitado foi: {}".format(media, maior))














