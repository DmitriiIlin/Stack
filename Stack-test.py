import unittest,random,Stack

def input_generation():
    i=random.randint(0,20)
    St=''
    for j in range(i):
        k=random.randint(1,2)
        if k==1:
            St=St+')'
        else:
            St=St+'('
  #  print(St)
    return(St)

def q_ty_St(St):
    St_len=len(St)
    St_first=0
    St_second=0
    output=[]
    for i in range(St_len):
        if St[i]==')':
            St_first+=1
        elif St[i]=='(':
            St_second+=1
    output.append(St_first)
    output.append(St_second)
    return output

#print(q_ty_St(input_generation()))


class Stack_tests(unittest.TestCase):

    def test_equal_q_ty_test(self):
        S=input_generation()
        Q_ty=q_ty_St(S)
        print(Q_ty[0])
        print(Q_ty[1])
        self.assertEqual(Stack.input_string(S)==True,Q_ty[0]==Q_ty[1])

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()  


