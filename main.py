#var = input('Write a name...')

#def functionTest(x):
       #print("Hello", x)

#def main():
   # var = input("Enter a name/n")
    #functionTest(var)
#if __name__ == 'main':  #de aflat de ce folodim sim conditia data
 #main()

#def calc(a, b):
   # print(a + b)  #Hello + name = Helloname
   # print(a - b)  #
   # print(a * b)  #Hello * 2 = HelloHello    #hello* string= illegal exception
    #print(a / b)

#a = int(input('Enter first number ...\n'))
#b = int(input('Enter second number...\n'))

#calc(a, b)



#def calc(*args):
    #print(args[0] + args[1])
   # print(args[0] - args[1])
    #print(args[0] * args[1])
   #print(args[0] / args[1])

#a = 2
#b = 3
#calc(a, b)

#def to_upper(word):
    #return word.upper()  #receive(primim result
#def to_uppercase(word):
    #print(word.upper())  #display(afisam result

#to_uppercase('hello')
#print(to_upper("hello"))

#for i in range(3, 5):
    #if i == 4:
       # print('dg')
        #continue # pentru a continua codul
        #break # pentru a opri codul

#def will_be_used_in_future()
   # pass #trece peste fara sa arunce RuntimeException (eroare)


max_hp = 100

player_hp = 100
player_life = 3
player_damage = 30
player_armor = 80
nr_hits = 1

player_name = input("Enter player name...\n")
def attack(player_hp, player_damage):
    global player_armor,  nr_hits, player_lifelife

    if player_armor - player_damage > 0:
        player_armor = player_armor - player_damage
    else:
        player_hp  = player_hp - player_damage
        if player_hp == 0:
            player_life = player_life - 1
            player_hp = max_hp
        return player_hp

def heal(player_hp, heal):
    global max_hp, player_life

    if player_hp + heal > max_hp:
        player_hp = max_hp
    else:
        player_hp = player_hp + heal
    return player_hp

#for i in range(1, 20):
    #if player_hp > 0:
       # player_hp = attack(player_hp, player_damage)
   # else:
       # break

   # print("Live ", player_hp)
   # print("Armor ", player_armor)
   # print("Hit nr", nr_hits)
#else:
  #  print("Draw")
#print("You are dead")


for i in range(1, 100):
    if player_hp > 0:
        nr_hits = nr_hits + 1

        if nr_hits % 3 == 0:
            pass
        else:
            player_hp = attack(player_hp, player_damage)

        print("____" + player_name + "___")
        print("Live", player_hp)
        print("Armor", player_armor)
        print("Hit nr", nr_hits)

    else:
        break

print("You are dead")








1234567890-0987654321
pers_name = input("Set the name ")
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1


def attack(pers_hp, dmg=10):
    global armor, nr_hits

    if armor - dmg > 0:
        armor = armor - dmg
    else:
        pers_hp = pers_hp - dmg
    return pers_hp


def heal(pers_hp, live):
    global max_pers_hp

    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp
    else:
        pers_hp = pers_hp + live

    return pers_hp


pers_hp = attack(pers_hp, 40)
print(pers_hp)

pers_hp = heal(pers_hp, 20)
print(pers_hp)

# Make a battle
for i in range(1, 100):

    if pers_hp > 0:
        pers_hp = attack(pers_hp)
    else:
        break

    print("Live ", pers_hp)
    print("Armor", armor)
    print("Hit nr ", i)

print("You are dead")

# Bonus
for i in range(1, 100):

    if pers_hp > 0:
        nr_hits = nr_hits + 1

        if nr_hits % 3 == 0:
            pass
        else:
            pers_hp = attack(pers_hp)
        print("----" + pers_name + "---")
        print("Live ", pers_hp)
        print("Armor", armor)
        print("Hit nr ", nr_hits)

    else:
        break
















