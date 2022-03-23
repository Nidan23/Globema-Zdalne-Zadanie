from collections import Counter

def SieveOfEratosthenes(n): # Tworzenie liczb z zakresu (123 456 789) i użycie sita Eratostelesa
     
    prime = [True for i in range(n + 1)]
    data = []
    p = 2
    while (p * p <= n):
         
        if (prime[p] == True):
             
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    prime[0]= False
    prime[1]= False

    for p in range(n + 1):
        if prime[p]:
            data.append(str(p))

    return data

def FindGroups(data): # Szukanie grup liczb pierwszysch podobnych

    for i in range(len(data)):
        temporaryData = []
        for chars in data[i]:
            temporaryData.append(chars)

        temporaryData = sorted(temporaryData)   # Sortowanie tymczasowej tablicy znaków

        data[i] = ''    # Usuwanie poprzedniej wartości

        for x in temporaryData:
            data[i] = data[i] + x   # Przypisywanie nowej wartości

    res = Counter(data)     # Zliczanie duplikatów - ilość liczb z danej grupy

    res = sorted(res.items(), key =
             lambda kv:(kv[1], kv[0]))      # Sortowanie

    print(f'Największa grupa to: {res[-1][0]} - {res[-1][1]} wystąpień')

if __name__=='__main__':
    n = 123456789

    FindGroups(SieveOfEratosthenes(n))