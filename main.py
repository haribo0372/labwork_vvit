p = 0
while p == 0 :
    try:
        t = int(input('Please enter 1 to continue or enter 2 to finish : '))
        if t == 1:
            try:

                print('Enter a')
                a = int(input())
                print('Enter b')
                b = int(input())
                print('Enter c')
                c = int(input())
                d = (b*b) - (4*a*c)
                if d > 0:
                    x1 = ((-1 * b) + (d**0.5)) / (2*a)
                    x2 = ((-1 * b) + (d**0.5)) / (2*a)
                    print('Discriminant :' , d, '\n' ,'The equation has two roots:' , '\n' , 'x1 = ',x1, '\n','x2 = ',x2)
                elif d == 0 :
                    x = (-1 * b)  / (2*a)
                    print('Discriminant :' , d, '\n' ,'The equation has one roots:','\n' , 'x = ',x)
                else :
                    print('The equation has no roots because the discriminant is less than zero :','\n', 'D = ',d , '\nD < 0')


            except ValueError:
                print('Please enter only the number')
            except ZeroDivisionError:
                print('Your equation is not with three unknowns')

            finally:
                print('\n\n\nSubscribe to our group :\nhttps://vk.com/bbteveryday')

        elif t == 2:
            break
        else:
            print("You're a fool , I'm sorry")
    except ValueError:
        break
