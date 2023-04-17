from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def dna(request):
    Seq,Seq2 = '',''
    A,T,C,G = 0,0,0,0
    if request.method == "POST":
        Seq = request.POST["DNASequencia"].upper()
        Seq2 = ""

        if all(i in 'ACGT' for i in Seq):
            for i in Seq:
                match i:
                    case "C":
                        Seq2 += "G"
                        C += 1
                    case "G":
                        Seq2 += "C"
                        G += 1
                    case "T":
                        Seq2 += "A"
                        T += 1
                    case "A":
                        Seq2 += "T"
                        A += 1
        else:
            if Seq == '':
                Seq2 = ''
            else:
                Seq = "SEQUÊNCIA INVÁLIDA, TENTE NOVAMENTE"

    return render(request, 'DNA.html', {
        "DNASequencia" : Seq,
        "DNAResultado" : Seq2,
        "A" : A,
        "T" : T,
        "C" : C,
        "G" : G,
    })

def terraPlana(request):
    Res = ""
    if request.method == "POST":
        Raio,Altura = request.POST["Raio"],request.POST["Altura"]
        Raio = int(Raio) if type(Raio)==str else 0
        Altura = int(Altura) if type(Altura)==str else 0

        Res = "%.2f" % (3.14 * Raio * Raio * Altura / 3)
        Res = f"Volume: {Res} Km3"
        

    return render(request, "terraPlana.html",{
        "Res" : Res
    })

def contarVogais(request):
    text = ""
    Vogais = ""
    A,E,I,O,U = 0,0,0,0,0
    if request.method == "POST":
        Vogais = 0
        text = request.POST["texto"]
        for i in text.lower():
            Vogais += 1 if i in 'aeiou' else 0
        if Vogais == 0:
            Vogais = ""
        else:
            Vogais = f"Há {Vogais} vogais no seu texto."

        for i in text.upper():
            match i:
                case "A":
                    A += 1
                case "E":
                    E += 1
                case "I":
                    I += 1
                case "O":
                    O += 1
                case "U":
                    U += 1


    return render(request, "contarVogais.html",{
        "Vogais" : Vogais,
        "A" : (f"Há {A} A no seu texto"),
        "E" : (f"Há {E} E no seu texto"),
        "I" : (f"Há {I} I no seu texto"),
        "O" : (f"Há {O} O no seu texto"),
        "U" : (f"Há {U} U no seu texto"),
    })

def matrizIdentidade(request):
    matriz = ""
    if request.method == "POST":
        Ordem = int(request.POST["ordemMatriz"]) if type(request.POST["ordemMatriz"])==str else 0
        matriz = ""
        for i in range(0, Ordem):
            for j in range(0, Ordem):
                matriz += "0 " if i!=j else "1 "
            matriz += "\n"

    return render(request, "matrizIdentidade.html",{
        "matriz" : matriz
    })

def fibonacci(request):
    FibonacciFinal = ""
    if request.method == "POST":
        try:
            indice = int(request.POST["indice"])
            FibonacciFinal = [0] * indice
            if indice >= 2:
                FibonacciFinal[1] = 1

            for i in range(indice):
                if i > 1:
                    FibonacciFinal[i] = FibonacciFinal[i-1] + FibonacciFinal[i-2]
            FibonacciFinal = str(FibonacciFinal[-1])
        except:
            FibonacciFinal = ""

    return render(request, "fibonacci.html",{
        "fibonacci" : FibonacciFinal
    })

    
