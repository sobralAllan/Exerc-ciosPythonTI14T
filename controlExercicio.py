from modelExercicio import modelExercicio

class controlExercicio:
    def __init__(self):
        self.model = modelExercicio()
        self.opcao = -1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\n\n\nEscolha uma das opções abaixo: \n" +
              "\n0. Sair"                         +
              "\n1. Exercício 01"                 +
              "\n2. Exercício 02"                 +
              "\n3. Exercício 03"                 +
              "\n4. Exercício 04"                 +
              "\n5. Exercício 05"                 +
              "\n6. Exercício 06"                 +
              "\n7. Exercicio 07"                 +
              "\n8. Exercício 08"                 +
              "\n9. Exercicio 09 "                +
              "\n10. Exercício 10"                +
              "\n14. Exercício 14"                +
              "\n18. Exercício 18")
        self.setOpcao(int(input()))

    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                print(self.model.exercicio01())
            elif self.getOpcao() == 2:
                print("Digite um valor: ")
                print(" o valor antecessor digitado foi: {}".format(self.model.exercicio02(int(input()))))
            elif self.getOpcao() == 3:
                print("Digite a base: ")
                base = float(input())
                while base <= 0:
                    if base <= 0:
                        print("Impossivel calcular!")
                        print("Digite a base: ")
                        base = float(input())

                print("Digite a altura:")
                altura = float(input())
                while altura <= 0:
                    if altura <= 0:
                        print("Impossivel calcular!")
                        print("Digite a altura:")
                        altura = float(input())

                print("O valor da área do retangulo é: {}".format(self.model.exercicio03(base, altura)))

            elif self.getOpcao() == 4:
                self.model.exercicio04()

            elif self.getOpcao() == 5:
                print("Digite o total de eleitores :")
                eleitores = int(input())
                while eleitores < 0:
                    if eleitores < 0:
                        print ("Número de eleitores inválido")
                        print("Digite o total de eleitores :")
                        eleitores = int(input())



                print("Digite o total de votos válidos :")
                vvalidos = int(input())
                while vvalidos < 0:
                      if vvalidos < 0:
                        print ("Número de votos inválido")
                        print("Digite o total de votos válidos :")
                        vvalidos = int(input())

                print("Digite o total de votos brancos :")
                vbrancos = int(input())
                while vbrancos < 0:
                    if vbrancos < 0:
                        print ("Número de votos inválido")
                        print("Digite o total de votos brancos :")
                        vbrancos = int(input())
                print("Digite o total de votos nulos :")
                vnulos = int(input())
                while vnulos < 0:
                    if vnulos < 0:
                        print ("Número de votos inválido")
                        print("Digite o total de votos nulos :")
                        vnulos = int(input())

                print(self.model.exercicio05(eleitores, vvalidos, vbrancos, vnulos))

            elif self.getOpcao() == 6:
                salario = 0
                reajuste = 0
                print("Digite o salário atual do funcionário: ")
                salario = float(input())
                while salario <= 0:
                    if salario <= 0:
                        print("Digite um valor positivo acima de 0")
                        print("Digite o salário atual do funcionário: ")
                        salario = float(input())

                print("Digite o percentual de reajuste: ")
                reajuste = float(input())

                while reajuste <= 0:
                    if reajuste <= 0:
                        print("Digite um valor positivo acima de 0")
                        print("Digite o percentual de reajuste: ")
                        reajuste = float(input())

                print("O novo salário do funcionário com reajuste é: {}".format(self.model.exercicio06(salario, reajuste)))

            elif self.getOpcao() == 7:
                print("Informe o custo de fabrica do veiculo:")
                num = float(input())
                while num < 0:
                    if num < 0:
                        print("Valor invalido!")
                        print("Informe o custo de fabrica do veiculo:")
                        num = float(input())
                print("O valor do veiculo é: {}".format(self.model.exercicio07(num)))
            elif self.getOpcao() == 8:
                print("Digite a primeira nota:")
                nota1 = float(input())
                while nota1 < 0 or nota1 > 10:
                    if nota1 < 0 or nota1 > 10:
                        print("Valor inválido. Tente novamente:")
                        print("Digite a primeira nota:")
                        nota1 = float(input())
                print("Digite a segunda nota:")
                nota2 = float(input())
                while nota2 < 0 or nota2 > 10:
                    if nota2 < 0 or nota2 > 10:
                        print("Valor inválido. Tente novamente:")
                        print("Digite a segunda nota:")
                        nota2 = float(input())
                print("Digite a terceira nota:")
                nota3 = float(input())
                while nota3 < 0 or nota3 > 10:
                    if nota3 < 0 or nota3 > 10:
                        print("Valor inválido. Tente novamente:")
                        print("Digite a terceira nota:")
                        nota3 = float(input())
                print("A média do aluno é: {}".format(self.model.exercicio08(nota1,nota2,nota3)))

            elif self.getOpcao() == 9:
                print("Digite  o total de macas: ")
                macas = int(input())
                while macas < 0:
                    if macas < 0:
                        print(" Valor Inválido!")
                        print("Digite  o total de macas: ")
                        macas =  int(input())

                print("O total  a Pagar é de: R${}".format(self.model.exercicio09(macas)))
            elif self.getOpcao() == 10:
                i = 0
                for i in range(10):
                    print("Informe o {}º número: ".format(i+1))
                    self.model.preencherVetor(int(input()))
                print("\nSem ordenação!...")
                self.model.visualizarVetor()

                print("\nCom ordenação!...")
                self.model.ordenar()

                print("\nRemovendo a posição 5 do vetor")
                self.model.excluir(5)
            elif self.getOpcao() == 14:
                print("Informe a quantidade de números que deseja ver: ")
                final = input()
                print(self.model.exercicio14(final))
            elif self.getOpcao() == 18:
                print("Informe a quantidade de números que deseja: ")
                quant = int(input())
                self.model.exercicio18(quant)
            else:
                print("Opção invalida!")