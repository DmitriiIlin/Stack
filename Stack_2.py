import Stack_mod 

def input_string(S):
    #Функция определяет кол-во символов типа ( или ) и проверяет рав-во кол-ва этих элементов
    string_len=len(S)
    output="True"
    index=0
    a=Stack_mod.Stack()
    if string_len % 2 != 0:
        output="False"
  #      print(output,"ПЧ")
    else:
        while index<string_len and output:
            if S[index]=="(":
                a.push(S[index])
            elif S[index]==")":
                if string_len==0:
                    output=="False"
                else:
                    a.pop()
            index+=1 
 #       print("ВЧ",output)
    return output 


r="))(((("
print(input_string(r))
