import Stack_mod 

def input_string(S):
    #Функция определяет кол-во символов типа ( или ) и проверяет рав-во кол-ва этих элементов
    string_len=len(S)
    first_simbol=S[0]
    a=Stack_mod.Stack()
    for i in range(string_len):
        print(S[i])
        if S[i]==first_simbol:
            a.push(S[i])
        else:
            if (a.size()==0) and (i!=(len(S)-1)):    
                first_simbol=S[i]
                a.push(S[i])
            else:
                a.pop()
    if a.peak()==None:
        output="True"
    else:
        output="False"
    return output
