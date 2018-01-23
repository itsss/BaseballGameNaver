# -*- coding: utf-8 -*-
import random

def get_random_number():
    return random.randrange(100, 1000)


def is_digit(user_input_number): #PASS
    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number): #PASS
    result = None
    inres = int(user_input_number)
    if inres >= 100 and inres <= 999:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit): #PASS
    return len(set(three_digit)) != 3


def is_validated_number(user_input_number): #PASS
    result = None;
    a = is_digit(user_input_number)
    if a == True:
        b = is_between_100_and_999(user_input_number);
        c = is_duplicated_number(user_input_number);
        if b == True and c == False :
            result = True
        else:
            result = False
    else:
        result = False
    return result

def get_not_duplicated_three_digit_number(): #PASS
    result = None
    rn = ["0", "0", "0"]
    rn[0] = str(random.randrange(1, 9, 1))
    rn[1] = rn[0]
    rn[2] = rn[0]
    while (rn[0] == rn[1]):
        rn[1] = str(random.randrange(1, 9, 1))
    while (rn[0] == rn[2] or rn[1] == rn[2]):
        rn[2] = str(random.randrange(1, 9, 1))
    result = rn[0]+rn[1]+rn[2]
    return result


def get_strikes_or_ball(user_input_number, random_number): #PASS
    result = [0, 0];
    for i in range(0, 3):
        for j in range(0, 3):
            if(user_input_number[i] == str(random_number[j]) and i == j):
                result[0] += 1;
            if(user_input_number[i] == str(random_number[j]) and i != j):
                result[1] += 1;
    return result


def is_yes(one_more_input): #PASS
    result = None
    if one_more_input[0] == "Y" or one_more_input[0] == "y" or one_more_input =="YES" or one_more_input == "Yes" or one_more_input == "yEs" or one_more_input == "yes":
        result = True
    else:
        result = False
    return result


def is_no(one_more_input): #PASS
    result = None
    if one_more_input == "N" or one_more_input == "n" or one_more_input =="NO" or one_more_input == "No" or one_more_input == "nO" or one_more_input == "no":
        result = True
    else:
        result = False
    return result


def main():
    print("Play Baseball")
    user_input = 999
    arr = [0, 0]
    while True:
        find = 0
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        while True :
            user_input = input('Input guess number : ')

            if str(user_input) == "0":
                print("Thank you for using this program")
                print("End of the Game")
                exit()

            if is_validated_number(user_input) == False:
                print("Wrong Input, Input again")

            else:
                arr = get_strikes_or_ball(random_number, user_input)
                print("Strikes : " + str(arr[0]) + " , Balls : " + str(arr[1]))
                if arr[0] >= 3:
                    while True:
                        chk = input('You win, one more(Y/N) ?')
                        if is_no(chk) == True:
                            print("Thank you for using this program")
                            print("End of the Game")
                            exit()
                        if is_yes(chk) == True:
                            find = 1
                            break
                        else:
                            print("Wrong Input, Input again")
                if find == 1:
                    break

if __name__ == "__main__":
    main()
