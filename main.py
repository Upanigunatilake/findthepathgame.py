print("Welcome to my first game")
name=input('what is your name?: ' )
age=input("what is your age?: ")

print("Hi",name," you are ", age," years old")
health=10

if int(age)>=18:
    print("you are old enough to play the game.")
    wants_to_play=input('do you want to play?').lower()
    if wants_to_play=='yes':
     print("let's play!")
     print("you are starting with",health," health")
     left_or_right= input('first choice......left?...or right?..... (choose left or right):')
     if left_or_right=='left':
             ans=input('nice....you go  ahead and reached a lake will you go around the lake or swim across the lake(choose around/across): ')
             if ans=='around':
                 print('cuz you went around the  lake to reach the other side of the lake')
             elif ans=='across':
                print('you were bit by a fish and lost five health')
                health-=5
             ans =input('you see a river and a house. where do you go to?...(river or house): ').lower()
             if ans== 'house':
                print('when you go to the house you are greeted by the owner.....and he does not like you and you got hit by him and you lost five health')
                health-=5
             if health <= 0:
                print('now you have zero health so you lost the game....')
             else:
                print('you have survived...... YOU ARE THE WINNER!!')
