def reverse(string): #переворот строки
    i = 0
    string2 = '' #объявление пустой строки
    for ch in range(len(string)):
        cnt = len(string) - i - 1 #перебор стркои в обратном порядке
        string2 = string2 + string[cnt] #добавляем к новой стркое символ
        i = i + 1
    print(string2)
reverse("hello, world")
