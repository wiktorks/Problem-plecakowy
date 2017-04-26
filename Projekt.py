import random as rand
import re

###########------------------------------Problem Plecakowy------------------------------###########

#item=(cena, waga)

def makeItems(n):
    items=[]
    for i in range(n):
        items.append((rand.randint(1, 20), rand.randint(1, 10)))
    return items

def createItems(n):
    items=[]
    for i in range(n):
        c = int(input("Podaj cene %s przedmiotu: "%str(i+1)))
        w = int(input("Podaj wage %s przedmiotu: "%str(i+1)))
        items.append((c, w))
    return items

def powerSet(items):
    pSet=[[]]
    for item in items:
        sol = [p + [item] for p in pSet]
        pSet.extend(sol)
    return pSet

def weight(item):
    return item[1]

def price(item):
    return item[0]

def cmp(item):
    return (float)(price(item)/weight(item))

def bruteForce(items, maxWeight):
    maxprice=0
    bestChoice=None
    items=powerSet(items)
    for item in items:

        currweight=sum([weight(w) for w in item])
        currprice=sum([price(p) for p in item])

        if currprice>maxprice and currweight<=maxWeight:
            maxprice = currprice
            bestChoice = item

    return bestChoice


def greedo(items, func, maxWeight):

    greed=sorted(items, key=func, reverse=True)
    sol=[]
    currweight=0
    for item in greed:
        currweight+=weight(item)
        if currweight>=maxWeight:
            break
        sol.append(item)
    return sol

###########------------------------------Szukanie palindromów------------------------------###########

def isPalindrome(word):
    i=0
    j=len(word)-1
    isPal=True
    while(i<j):
        if word[i]!=word[j]:
            isPal=False
            break
        i+=1
        j-=1
    return isPal

def findWords(line):
    word=""
    words=[]
    for i in range(len(line)-1):
        letter=line[i]
        if re.search(r'[a-zA-Z]', letter) \
                or letter=='ą' \
                or letter=='ć' \
                or letter=='ę' \
                or letter=='ó' \
                or letter=='ś' \
                or letter=='ł' \
                or letter=='ń' \
                or letter=='ż' \
                or letter=='ź':
            word+=letter
        else:
            if len(word)>=3:
                words.append(word)
            word=""
    return words

def findPalindromes(content):
    words=findWords(content)
    palindromes=[]
    for word in words:
        if isPalindrome(word):
            palindromes.append(word)
    return palindromes

def mainMenu():
    print("---------|Co chcesz robic?|---------")
    print("|                                  |")
    print("|1. Algorytm plecakowy             |")
    print("|                                  |")
    print("|2. Palindromy w tekscie           |")
    print("|                                  |")
    print("|3. Wyjscie                        |")
    print("|__________________________________|")

def knapsackMenu():
    print("--------|Wybierz algorytm:|---------")
    print("|                                  |")
    print("|1. Brute force                    |")
    print("|                                  |")
    print("|2. Zachłanny                      |")
    print("|                                  |")
    print("|3. Obydwa                         |")
    print("|                                  |")
    print("|4. Powrot                         |")
    print("|__________________________________|")

def knapsackMenu1():
    print("--------|Wybor przedmiotow:|--------")
    print("|                                  |")
    print("|1. Wprowadz przedmoity            |")
    print("|                                  |")
    print("|2. Losuj przedmioty               |")
    print("|__________________________________|")

def runKnapsack(choice):
    items=None
    while(True):
        knapsackMenu1()
        choice1 = int(input())
        if choice1==1:
            n=int(input("Ile chcesz przedmiotow?"))
            items=makeItems(n)
            break
        elif choice1==2:
            n = int(input("Ile chcesz przedmiotow?"))
            items=createItems(n)
            break
        else:
            print("Niepoprawny wybor")
    maxWeight=int(input("Podaj max wage"))
    print("Przedmoioty do spakowania: ", items)
    if choice==1:
        print("Algorytm silowy problemu plecakowego:")
        print(bruteForce(items, maxWeight))
    elif choice==2:
        print("Algorytm zachlanny problemu plecakowego:")
        print(greedo(items, cmp,  maxWeight))
    else:
        print("Silowy: ", end=' ')
        print(bruteForce(items, maxWeight))
        print("Zachlanny: ", end=' ')
        print(greedo(items, cmp, maxWeight))

def main():

    while(True):
        mainMenu()
        choice=int(input())
        if choice==1:
            while(True):
                knapsackMenu()
                choice = int(input())
                if choice>=1 and choice<=3:
                    runKnapsack(choice)
                elif choice==4:
                    break
                else:
                    print("Niepoprawny wybor")
        elif choice==2:
            palindromes = []
            with open("tekst.txt") as r:
                for line in r:
                    content = line.rstrip('\n')
                    words = findPalindromes(content)
                    if words != []:
                        palindromes += words[:]
            print(palindromes)
        elif choice==3:
            print("Wyjscie")
            break
        else:
            print("niewlasciwy wybor")


if __name__=="__main__":
	main()
