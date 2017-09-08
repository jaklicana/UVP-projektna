import random
vislice = ['''
  
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
 
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''', '''
 
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']
words = 'sevilla nerja valencia madrid malaga gibraltar alex eva kri cordoba granada alicante'.split()

def nakljucna_beseda(seznam_besed):
    besedni_indeks = random.randint(0, len(seznam_besed) - 1)
    return seznam_besed[besedni_indeks]

def prikazi_tablo(vislice, napacne_crke, pravilne_crke, resitev):
    print(vislice[len(napacne_crke)])
    print()
    
    print('Napačne črke:', end=' ')
    for letter in napacne_crke:
        print(letter, end=' ')
    print()
     
    blanks = '_' * len(resitev)
    
    for i in range(len(resitev)): 
        if resitev[i] in  pravilne_crke:
            blanks = blanks[:i] + resitev[i] + blanks[i+1:]
     
    for letter in blanks: 
        print(letter, end=' ')
        print()
    
def ugani(ze_ugibano):
        while True:
            print('Ugani črko.')
            ugib = input()
            ugib = ugib.lower()
            if len(ugib) != 1:
                print('Ugani samo ENO črko.')
            elif ugib in ze_ugibano:
                print('To črko si že uganil. Ugibaj še enkrat')
            elif ugib not in 'abcčdefghijklmnopqrsštuvwxyzž':
                 print('Ugani ČRKO.')
            else:
                return ugib
     
def igraj_se_enkrat():
         print('Bi rad igral še enkrat? (da ali ne')
         return input().lower().startswith('d')
    
    
print('VISLICE')
napacne_crke = ''
pravilne_crke = ''
resitev = nakljucna_beseda(words)
konec_igre = False

while True:
    prikazi_tablo(vislice, napacne_crke, pravilne_crke, resitev)

    ugib = ugani(napacne_crke + pravilne_crke)

    if ugib in resitev:
        pravilne_crke = pravilne_crke + ugib
        
        vse_crke_najdene = True
        for i in range(len(resitev)):
            if resitev[i] not in pravilne_crke:
                vse_crke_najdene = False
                break
        if vse_crke_najdene:
             print('Čestitam! Uganil si "' + resitev + '"!')
             konec_igre = True
    else:
        napacne_crke = napacne_crke + ugib       

        
    if len(napacne_crke) == len(VISLICE) - 1:
        prikazi_tablo(VISLICE, napacne_crke, pravilne_crke, resitev)
        print('Zmanjkalo ti je poskusov.!\nPo' + str(len(napacne_crke) + ' napacnih poskusih in' + str(len(pravilne_crke)) + ' pravilnih poskusih, je bila resitev beseda "' + resitev + '"')
        konec_igre = True

