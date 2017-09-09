import random
import time

print("VISLICE")
#pozdrav 
ime = input("Kako ti je ime?")

print('Živjo, ' + ime + '! Čas je za igro vislic!')

print (" ")

#počakaj 1s
time.sleep(1)

print("""Prosim izberi kategorijo.
Izbiraš lahko med temami: živali, barve..
Vnesi z za živali, b za barve.
Začni z ugibanjem...""")
time.sleep(0.5)

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
seznam_besed = ['letalo', 'kozarec']
zivali = ['zebra', 'medved', 'riba']
barve = ['modra', 'zelena', 'rumena']


def nakljucna_beseda(seznam_besed):
    besedni_indeks = random.randint(0, len(seznam_besed) - 1)
    return seznam_besed[besedni_indeks]

def nakljucna_beseda(zivali):
    zivali_indeks = random.randint(0, len(zivali) - 1)
    return zivali[zivali_indeks]

def nakljucna_beseda(barve):
    barve_indeks = random.randint(0, len(barve) - 1)
    return barve[barve_indeks]

  
# funkcija prikazi_tablo nariše stanje vislic
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
        
# kontrola izbire črke    
def ugani(ze_ugibano):
        while True:
            print('Ugani črko.')
            ugib = input()
            ugib = ugib.lower()
            if len(ugib) != 1:
                print('Ugani samo ENO črko.')
            elif ugib in ze_ugibano:
                print('To črko si že uganil. Ugibaj še enkrat')
            elif ugib not in 'abcčdđefghijklmnopqrsštuvwxyzž':
                 print('Ugani ČRKO.')
            else:
                return ugib

#tukaj vprašamo uporabnika naj vnese začetno črko za kategorijo, če izbere napačno črko mu vrže ven eno izmed seznam_besed
if input().lower().startswith('z'):
        resitev = nakljucna_beseda(zivali)
else:
        resitev = nakljucna_beseda(seznam_besed)
              
# funkcija igraj je ena iteracaija igre vislice
def igraj():
    print('VISLICE ')
# Definicija spremenjljivk    
    napacne_crke = ''  # seznam napačnih črk
    pravilne_crke = '' # seznam pravilno uganjenih črk
    resitev = nakljucna_beseda(seznam_besed) # naključen izbor besede za ugibanje
    konec_igre = False # izhod iz igre
    while konec_igre == False:
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
        if len(napacne_crke) == len(vislice) - 1:
            prikazi_tablo(vislice, napacne_crke, pravilne_crke, resitev)
            print('Zmanjkalo ti je poskusov.!\nPo ' + str(len(napacne_crke)) + ' napacnih poskusih in ' + str(len(pravilne_crke)) + ' pravilnih poskusih, je bila rešitev beseda "' + resitev + '"')
            konec_igre = True


# igranje dokler je odgovor Da
igraj_se_enkrat = True
while igraj_se_enkrat:
    igraj()
    print('Bi rad igral še enkrat? (da ali ne)')
    odgovor = input().lower().startswith('d')
    if odgovor == 'd':
        igraj_se_enkrat == True
    else:
        igraj_se_enkrat == False
    
