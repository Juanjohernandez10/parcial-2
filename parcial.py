# This program registers new members for a soccer team

my_dictionary = {}
import os
sw = True
Counter = 0
counter_goalkeeper =0
counter_defending = 0
counter_midfielder = 0
counter_Forward = 0
def fnt_clean ():
    os.system('cls')
    print("-------Welcome to the Soccer Team Registration Program----------")
    print('\n')
    print('FOUNDER: JUAN JOSE HERNANDEZ DUARTE ')
    



def fnt_add(dictionary, id_person, name, age, city,position):
    if id_person == '' or name == '' or age == '' or city == '' or position == '':
        enter = input('You must fill out all the requested information <ENTER>')
    else:
        dictionary[id_person] = {'name': name, 'age': age, 'city': city, 'position':position}
        enter = input(f'\nThe person  {name} has been successfully registered <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        name = input('NAME:  ')
        age = int(input('AGE:  ')) 
        if age >= 3 and age <=5:
            print('category sub 6')
        elif age >= 6 and age <= 8:
            print('category sub 8')
        elif age >=9 and age <= 12:
            print('category sub 10')
        elif age >= 13 and age<= 16:
            print('category sub 14')
        elif age >=17 and age <= 19:
            print('category sub 17 ')
        city = input('CITY:  ')
        id = int(input('Id: '))
        p= True
        while p== True:
            global counter_goalkeeper
            global counter_defending
            global counter_midfielder
            global counter_Forward
            print('the player´s position is?')
            position = input('\n1.goalkeeper\n2.defending\n3.midfielder\n4.Forward\n->')
            if position == '1':
                counter_goalkeeper +=1
                print(f'position is goalkeeper, amount: {counter_goalkeeper} ')
                break
            elif position == '2':
                counter_defending += 1
                print(f' position is defending, amount: {counter_defending} ')
                break
            elif position == '3':
                counter_midfielder += 1
                print(f'position is midfielder, amount: {counter_midfielder}')
                break
            elif position =='4':
                counter_Forward += 1
                print(f'position is Forward, amount: {counter_Forward}')
                break
            
        
        
        fnt_add(my_dictionary, id, name, age, city,position)
        

    

while sw == True:
    fnt_clean()
    print('\n')
    opcion = input('1. check in\n2. show\n3. exit\n- >  ')
    if opcion == '1':
        fnt_selector(opcion)
        
    elif opcion == '2':
        
        os.system('cls')
        print('\nnumber of records: ',len(my_dictionary),'\n')
        for clave, valor in my_dictionary.items():
            print(f"{clave}: {valor}")
        Counter += 1
        print(f'person´s counter: -> {Counter}')
        
        enter = input('\n\n input ENTER to continue...')
   
        
    elif opcion == '3':
        break