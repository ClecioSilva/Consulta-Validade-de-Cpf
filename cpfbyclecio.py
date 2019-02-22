print("=============================================================================")
print("=                  PROGRAMA PARA VERIFICAR VALIDADE DE CPF                  =")
print("=============================================================================")
print("                                                                    By Clecio")
denovo = "S"
while denovo == "S":
    cpf = input("\nDigite aqui o cpf sem pontos e traço: ")
    tamanho=len(cpf)
    if tamanho > 11 or tamanho < 11:
        print("\nVocê digitou mais de 11 ou menos de 11 digitos")
        denovo= str(input("\nTentar novamente [S/N] ? ")).upper()
    else:
        #caso esteja correto
        
        #primeiro digito verificador
        primeiro= int(cpf[0])
        segundo = int(cpf[1])
        terceiro = int(cpf[2])
        quarto = int(cpf[3])
        quinto = int(cpf[4])
        sexto = int(cpf[5])
        setimo = int(cpf[6])
        oitavo = int(cpf[7])
        nono = int(cpf[8])

        mult1 = int(10*primeiro)
        mult2 = int(9*segundo)
        mult3 = int(8*terceiro)
        mult4 = int(7*quarto)
        mult5 = int(6*quinto)
        mult6 = int(5*sexto)
        mult7 = int(4*setimo)
        mult8 = int(3*oitavo)
        mult9 = int(2*nono)
        
        somaprimeiro = int(mult1)+int(mult2)+int(mult3)+int(mult4)+int(mult5)+int(mult6)+int(mult7)+int(mult8)+int(mult9)
        restoprimeiro = int(somaprimeiro) % 11       
        resultadoprimeiro = 11 - int(restoprimeiro)
        

        #segundo digito verificador
        primeiro2= int(cpf[0])
        segundo2 = int(cpf[1])
        terceiro2 = int(cpf[2])
        quarto2 = int(cpf[3])
        quinto2 = int(cpf[4])
        sexto2 = int(cpf[5])
        setimo2 = int(cpf[6])
        oitavo2 = int(cpf[7])
        nono2 = int(cpf[8])
        decimo2 = int(cpf[9])

        mult12 = int(11*primeiro)
        mult22 = int(10*segundo)
        mult32 = int(9*terceiro)
        mult42 = int(8*quarto)
        mult52 = int(7*quinto)
        mult62 = int(6*sexto)
        mult72 = int(5*setimo)
        mult82 = int(4*oitavo)
        mult92 = int(3*nono)
        mult102 = int(2*decimo2)
        
        somasegundo = int(mult12)+int(mult22)+int(mult32)+int(mult42)+int(mult52)+int(mult62)+int(mult72)+int(mult82)+int(mult92)+int(mult102)
        restosegundo = int(somasegundo) % 11       
        resultadosegundo = 11 - int(restosegundo)
        if resultadoprimeiro == int(cpf[9]) and resultadosegundo == int(cpf[10]):
            print('\nCPF VÁLIDO')
        else:
            print("\nCPF INEXISTENTE")
        denovo= str(input("\nTentar outro CPF [S/N] ? ")).upper()
