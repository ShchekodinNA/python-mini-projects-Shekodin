import arts
import random
import os
clbrts = [
    {
        "name": "Some_man",
        "descr": "Live in middle of nowere",
        "flwrs": 85621
    },
    {
        "name": "Aaron Carter",
        "descr": "The 34-year-old musician",
        "flwrs": 515512
    },
    {
        "name": "Reese Witherspoon",
        "descr": "American actress and producer known for Legally Blonde, Sweet Home Alabama",
        "flwrs": 12151
    },
    {
        "name": "Jackie Chan",
        "descr": "Jackie Chan, is a Hong Kong-born Chinese actor, filmmaker",
        "flwrs": 515122
    },
    {
        "name": "Chris Tucker",
        "descr": "American comedian and actor",
        "flwrs": 5152125
    },
    {
        "name": "Jet Li",
        "descr": "Chinese film actor, film producer, martial artist",
        "flwrs": 15121
    },
    {
        "name": "Sylvester Stallone",
        "descr": "American actor, screenwriter, director, and producer.",
        "flwrs": 5125152
    },
    {
        "name": "Brandon Lee",
        "descr": "American actor and martial artist.",
        "flwrs": 9999
    },
]

def get_info( lv_clbr = {}):
    return (f"{lv_clbr['name']}. {lv_clbr['descr']}")

def gen_2_sides(lft_c, rght_c):
    if lft_c == None:
        lft_c = random.choice(clbrts)
    while True:
        rght_c = random.choice(clbrts)
        if clbrts.index(rght_c) != clbrts.index(lft_c):
            return lft_c, rght_c
        
def is_lft_bigger_rght(lft_c, rght_c):
    if lft_c["flwrs"] >= rght_c["flwrs"]:
        return True
    return False
    
contin = True
score = 0
left_c = None
right_c = None
while contin:
    os.system("cls")
    left_c, right_c = gen_2_sides(right_c,left_c)
    print(arts.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(f"compare A:{get_info(left_c)}\nvs\nAgainst B:{get_info(right_c)}")
    user_des = input("Who has more followers? Type 'A' or 'B': ").upper()
    compare_result = is_lft_bigger_rght(left_c,right_c)
    if user_des == "A" and compare_result :
        score += 1
    elif user_des == "B" and not compare_result:
        score += 1
    else:
        print(f"You were wrong. Score: {score}")
        quit()
        
    
    
    