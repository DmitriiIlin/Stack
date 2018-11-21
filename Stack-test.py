import unittest,random,Stack,Stack_1,Stack_2

def input_generation():
    i=random.randint(1,20)
    i=12
    print(i,"длина строки")
    St=''
    for j in range(i):
        k=random.randint(1,2)
        if j==0:
            k==2
        if k==1:
            St=St+')'
        else:
            St=St+'('
    print(St)
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

    def test_equal_q_ty_Stack(self):
        S=input_generation()
        Q_ty=q_ty_St(S)
        print(Q_ty[0],"Q-ty of sample 1 in Test 1")
        print(Q_ty[1],"Q-ty of sample 2 in Test 1")
        self.assertEqual(Stack.input_string(S)=="True",Q_ty[0]==Q_ty[1])

    def test_equal_q_ty_Stack_1(self):
        S=input_generation()
        Q_ty=q_ty_St(S)
        print(Q_ty[0],"Q-ty of sample 1 in Test 2")
        print(Q_ty[1],"Q-ty of sample 2 in Test 2")
        self.assertEqual(Stack_1.input_string(S)=="True",Q_ty[0]==Q_ty[1]) 
    
   # def test_equal_q_ty_Stack_2(self):
    #    S=input_generation()
     #   Q_ty=q_ty_St(S)
      #  print(Q_ty[0],"Q-ty of sample 1 in Test 2")
      #  print(Q_ty[1],"Q-ty of sample 2 in Test 2")
      #  self.assertEqual(Stack_2.input_string(S)=="True",Q_ty[0]==Q_ty[1])

if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()  


