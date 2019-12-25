def get_largest_perimiter(L):
    a = -1
    for i in range(len(L)-2):
        if (L[i] < 0):
            return "Неверные данные"
        for j in range(i+1,len(L)-1):
            if (L[j] < 0):
                return "Неверные данные"
            for k in range(j+1,len(L)):
                if (L[k] < 0):
                    return "Неверные данные"
                if (L[k]+L[i]>L[j] and L[k]+L[j]>L[i] and L[i]+L[j]>L[k]):
                    b = L[i]+L[k]+L[j]
                    if (b > a):
                        a = b
                        pos_b = j
                        dlin_b = L[j]
                        pos_a = i
                        dlin_a = L[i]
                        pos_c = k
                        dlin_c = L[k]

    if (a == -1):
        return "Таких треугольников нет"
    return ("Периметр искомого треугольника = " + str(a))


L = list(map(int, input().split()))
print(get_largest_perimiter(L))
