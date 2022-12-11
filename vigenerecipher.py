# Aluna: Luiza de Araújo Nunes Gomes
# Matrícula: 190112794

from math import ceil
import unicodedata

vigenereTable = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], 
    ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"], 
    ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"], 
    ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C"], 
    ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"], 
    ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E"], 
    ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F"], 
    ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G"], 
    ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H"], 
    ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I"], 
    ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
    ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"], 
    ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"], 
    ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"], 
    ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"], 
    ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"], 
    ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"], 
    ["R", "S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"], 
    ["S", "T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"], 
    ["T", "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"], 
    [ "U", "V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"], 
    ["V", "W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"], 
    ["W", "X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"], 
    ["X", "Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"], 
    ["Y", "Z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"], 
    ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]] 
alphabet = vigenereTable[0]

# Esta função passa os dados dos txts em string    
def get_data_from_txt(file):
    data = []
    with open(file, 'r') as projectfile:
        for line in projectfile:
            line = line.replace("\n", "")
            data.append(line)
    return " ".join(data)

# Esta função passa as letras do alfabeto EN em número de 0 a 25 de acordo com suas posições
def alphabet_to_number(letter):
    return(alphabet.index(letter))

# Esta função passa o número de 0 a 25 a letra do alfabeto EN
def number_to_alphabet(number):
    return(alphabet[number])

# Esta função identifca o número da letra de acordo com o index da fileira em que pertence
def number_to_rowIndex(letter, row):
    return(row.index(letter))

# Passa a palavra chave para a chave que auxilia na encriptação da cifra, a frase intermediária entre a cifra e a mensagem
def keyword_into_key(keyword, message):
    key = []
    times = ceil(len(message)/len(keyword))
    key = keyword*times
    key = key[:len(key) - (len(key)-len(message))]
    return key

# Esta função identifa a frequência que uma certa string aparece em uma lista de palavras
def frequency_of_strings(listOfWords):
    frequencyList = []
    for word in listOfWords:
        frequencyList.append([word, listOfWords.count(word)])
    norep = []
    [norep.append(x) for x in frequencyList if x not in norep]
    return sorted(norep, key = lambda x:x[1], reverse=True)

# Esta função separa um texto em diversos pedaços de um valor 'n',
# exemplo: cipher = 'algumtempo', e n = 5, vira 'algum lgumt gumte umtem mtemp tempo'.
def make_lots_of_nchunks(cipher, n):
    text = [x for x in unicodedata.normalize('NFKD', cipher.upper()) if x.isalpha()]
    text2 = []
    for x in range(len(text)-(n-1)):
        text2.append("".join(text[x:x+n]))
    return text2 

# Nesta função temos que ele identifca a posição de uma certa sequência em um texto
def positions_for_repeated_sequencies(sequency, textdivided):
    sequencyPositions = []
    for x in range(len(textdivided)):
        if textdivided[x] == sequency:
            sequencyPositions.append(x)
    return sequencyPositions

# Nesta função temos que este identifica a distância de sequências repetidas
def distances_for_repeated_sequencies(positions):
    size = len(positions)
    sequencyDistances = []
    for pos in range(size):
        if pos > 0:
            sequencyDistances.append(positions[pos] - positions[pos-1])
    return sequencyDistances

# Esta função realiza a conta de acordo com a repetição e a distância de acordo com fatores comuns
def factors_and_distances(distances):
    commonFactors = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]   #fatores comuns possíveis
    factorsList = []
    for d in distances:
        factors = []
        for i in range(1, int(d) + 1):
            if d % i == 0:
                factors.append(i)
        factorsList.append(factors)
    frequency = []
    for cf in commonFactors:
        cff = 0
        for x in factorsList:
            for f in x: 
                if f == cf:
                    cff = cff + 1
        frequency.append([cf, cff])
    sortedFrequency = sorted(frequency, key = lambda x:x[1], reverse=True)
    highest = 0
    morethantwice = []
    for sf in sortedFrequency:
        if sf[1] >= highest:
            morethantwice.append(sf)
            highest = sf[1]
            number = sf[0]
        elif sf[1] > 2:
            morethantwice.append(sf)
    return(morethantwice) 

# Esta função junta todos os elementos das funções anteriores, e realiza o cálculo da Frequência de Kasiski para descobrir
# quais é o tamanho das sequências que mais se repetem, mas se não há repetições, este retorna em uma lista de possíveis
# fatores comuns para facilitar o encontro do possível tamanho da chave
def kasiski_frequency(cipher):
    chunkof3 = make_lots_of_nchunks(cipher, 3)
    chunkof3f = frequency_of_strings(chunkof3)
    morethantwice = [x for x in chunkof3f if x[1]> 2]
    distancesList = []
    for x in morethantwice:
        for x in distances_for_repeated_sequencies(positions_for_repeated_sequencies(x[0], chunkof3)) :
            if x not in distancesList:
                distancesList.append(x)
    return (factors_and_distances(distancesList))

# Aqui temos uma função que passa a cifra/coset para o novo alfabeto de acordo com a mudança de cifra/coset
def cipher_shift(cipher, alphabetShift):
    sample = make_lots_of_nchunks(cipher, 1)
    new = []
    for s in sample:
        new.append(alphabetShift[alphabet_to_number(s)])
    return new

# Para usarmos o método X2-Frequency utiliza-se os cosets, que são divisões de um texto de acordo com uma quantidade 'n' de
# cosets, no caso da X2-Frequency temos que separar o texto em um número de cosets igual ao tamanho da chave
def cosets(cipher, keywordLength):
    c = make_lots_of_nchunks(cipher, 1)
    cosets = []
    for x in range(keywordLength):
        cosets.append([])
    for x in range(keywordLength):
        basis = x
        for y in range(len(c)):
            if y == basis:
                cosets[x].append(c[y])
                basis = basis + keywordLength
    return cosets   

# Nesta função temos o cálculo de x2  de um coset/cifra para cada letra do alfabeto
def x2frequency(cipher):
    FrequenciesEnglish = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.0228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
    cipherShifts = []
    A = []
    for x in range(26):
        if x == 0:
            A.append(vigenereTable[x])
            cipherShifts.append(cipher_shift(cipher, A[x]))
        elif x == 1:
            A.append(vigenereTable[25])
            cipherShifts.append(cipher_shift(cipher, A[x]))
        else:
            A.append(vigenereTable[25-x + 1])
            cipherShifts.append(cipher_shift(cipher, A[x]))
    frequencies = []
    for cipherShift in cipherShifts:
        Fx = []
        for a in alphabet:
            count = 0
            for letter in cipherShift:
                if a == letter:
                    count = count + 1
            Fx.append(float("%.4f"%(count/len(cipherShift))))
        frequencies.append(Fx)
    X2list = []
    for b in range(26):
        x = []
        for a in range(len(alphabet)):
            x.append(((frequencies[b][a] - FrequenciesEnglish[a])**2)/FrequenciesEnglish[a])
        total = 0
        for y in x:
            total = total + y
        X2list.append(total)
    return X2list

# Aqui analismos os valores encontrados no cálculo da frequência em X2, retornando assim os maiores valores e as respectivas
# letras do menor ao maior x2 encontrado para cada cifra/coset, realizando assim o método X2 de recuperação de palavras-chave.
def x2frequency_analysis(cipher, keywordLength):
    cosetsList = cosets(cipher, keywordLength)
    x2list = []
    for n in range(len(cosetsList)):
        x2list.append(x2frequency("".join(cosetsList[n])))
    x2Analysed = []
    for coset in x2list:
        pos = 0
        highestToLowestX2 = []
        for x in coset:
            highestToLowestX2.append([number_to_alphabet(pos), x])
            pos = pos + 1
        highestToLowestX2 = sorted(highestToLowestX2, key = lambda x:x[1], reverse=False)
        x2Analysed.append(highestToLowestX2)
    return x2Analysed

# Este é um codificador simples de uma cifra de Vigenere utilizando uma tabela de vigenere
def vigenere_encoder(message, keyword):
    messageList = [x for x in unicodedata.normalize('NFKD', message.upper()) if x.isalpha()]
    keywordList = [x for x in keyword.upper() if x.isalpha()]
    key = keyword_into_key(keywordList, messageList)
    ciphertext = []
    for i in range(len(key)):
        index_key = alphabet_to_number(key[i])
        for j in range(len(messageList)):
            index_message = alphabet_to_number(messageList[j])
            if i == j:
                ciphertext.append(vigenereTable[index_key][index_message])
    return ("".join(ciphertext)).lower()

# Este é um decodificador simples de uma cifra de Vigenere utilizando uma tabela de vigenere
def vigenere_decoder(cipher, keyword):
    cipherList = [x for x in unicodedata.normalize('NFKD', cipher.upper()) if x.isalpha()]
    keywordList = [x for x in keyword.upper() if x.isalpha()]
    decodedMessage = []
    key = keyword_into_key(keywordList, cipherList)
    for i in range(len(key)):
        index_key = alphabet_to_number(key[i])  
        index_cipher = number_to_rowIndex(cipherList[i], vigenereTable[index_key])
        decodedMessage.append(number_to_alphabet(index_cipher))
    return ("".join(decodedMessage)).lower()

# Este é um solucionador de cifras de Vigenere utilizando uma tabela de vigenere, Frequência de Kasiski para encontrar possíveis
# valores do tamanho das chaves, e Frequência X2 para encontrar cada letra de cada posição da palavra-chave.
# Esta função é interativa, então para encontrar a solução, o usuário deve se relacionar com a função para mudar os valores de
# acordo com sua vontade.
def vigenere_solver(cipher):
    possibleKeySizes = []
    for kf in kasiski_frequency(cipher):
        possibleKeySizes.append(kf[0])
    for n in possibleKeySizes:
        x2list = x2frequency_analysis(cipher, n)
        possible = []
        positions = []
        for x2 in x2list:
            positions.append(0)
            possible.append(x2[0][0])
        ok = 0
        while (ok == 0):
            solution = "".join(possible)
            print("\nA chave da encriptação formada foi:", solution)
            print("\nEncriptando a CIFRA com esta CHAVE temos:\n", vigenere_decoder(cipher, solution))
            good = input("\nA solução está satisfatória? (Digite SIM' ou 'NÃO) => ")
            if good == 'SIM':
                ok = 1
                text_file = open("solvedcipher.txt", "w")
                n = text_file.write(vigenere_decoder(cipher, solution))
                text_file.close()
                return vigenere_decoder(cipher, solution)
            elif good == 'NÃO':
                good = input("\nGostaria de mudar alguma letra da CHAVE proposta? Se NÃO aumentaremos a quantidade de letras da CIFRA (Digite SIM ou NÃO) => ")
                if good == 'SIM':
                    letter = input("\nQual letra? Digite a posição desta. (A primeira letra está no posição 0) => ")
                    question = input("\nGostaria de indicar alguma letra em específico? (Se sim indique a letra, se não, escreva NÃO) => ")
                    if question == 'NÃO':
                        positions[int(letter)] = positions[int(letter)] + 1
                        possible[int(letter)] = x2[positions[int(letter)]][0]
                        continue
                    elif question.isalpha():
                        possible[int(letter)] = question.upper()
                        continue
                elif good == 'NÃO':
                    ok = 1
                    continue


#Codificação e Decodificação respectivamente
print("Encodificando a frase 'ALL IS WELL' e com a chave 'CAKE' => ", vigenere_encoder("ALL IS WELL", "CAKE"))
print("Encodificando a frase 'YITZU GRFFE TZZOC GSITS XUEAH EIKUT P', e com a chave 'MARS' => ", vigenere_decoder("YITZU GRFFE TZZOC GSITS XUEAH EIKUT P", "MARS"))
#Desafios
cipher = get_data_from_txt('desafio1.txt')
vigenere_solver(cipher)
cipher = get_data_from_txt('desafio2.txt')
vigenere_solver(cipher)
