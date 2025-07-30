import numpy as np

class basic:
    keypad = np.array([[1,2,3], [4,5,6], [7,8,9], ['*',0,'#']])
    Rhand_pos = [3,2]
    Lhand_pos = [3,0]
    answer = []

def select_hand(R_dis, L_dis, hand, keypos_row):
    if (R_dis < L_dis): 
        basic.answer.append('R')
        basic.Rhand_pos = [keypos_row,1]
                
    elif (R_dis > L_dis):
        basic.answer.append('L')
        basic.Lhand_pos = [keypos_row,1]
                        
    else:
        if(hand == "right"):
            basic.answer.append('R')
            basic.Rhand_pos = [keypos_row,1]
                    
        if(hand == "left"):
            basic.answer.append('L')
            basic.Lhand_pos = [keypos_row,1]
    
def solution(numbers, hand):
    for key in numbers:
        match key:
            case 1 | 4 | 7:
                basic.answer.append('L')
                for i in range(3):
                    if (basic.keypad[i][0] == str(key)): basic.Lhand_pos = [i,0]
            case 3 | 6 | 9:
                basic.answer.append('R')
                for i in range(3):
                    if (basic.keypad[i][2] == str(key)): basic.Rhand_pos = [i,2]
            case 2:
                R_dis = abs(basic.Rhand_pos[0] - 0) + abs(basic.Rhand_pos[1] - 1)
                L_dis = abs(basic.Lhand_pos[0] - 0) + abs(basic.Lhand_pos[1] - 1)
                select_hand(R_dis, L_dis, hand, 0)                
            case 5:
                R_dis = abs(basic.Rhand_pos[0] - 1) + abs(basic.Rhand_pos[1] - 1)
                L_dis = abs(basic.Lhand_pos[0] - 1) + abs(basic.Lhand_pos[1] - 1)
                select_hand(R_dis, L_dis, hand, 1)
            case 8:
                R_dis = abs(basic.Rhand_pos[0] - 2) + abs(basic.Rhand_pos[1] - 1)
                L_dis = abs(basic.Lhand_pos[0] - 2) + abs(basic.Lhand_pos[1] - 1)
                select_hand(R_dis, L_dis, hand, 2)
            case 0:
                R_dis = abs(basic.Rhand_pos[0] - 3) + abs(basic.Rhand_pos[1] - 1)
                L_dis = abs(basic.Lhand_pos[0] - 3) + abs(basic.Lhand_pos[1] - 1)
                select_hand(R_dis, L_dis, hand, 3)
    
    answer = basic.answer
    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    result = solution(numbers, hand)
    print(result) # Output the answer as a string