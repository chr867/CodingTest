def solution(bandage, health, attacks):
    answer = 0
    successCount = 0
    lastSec = attacks[-1][0] + 1
    healthMaximum = health
    
    for i in range(lastSec):
        if health <= 0:
            return -1
        else:
            for j in attacks:
    #           공격하는 시간일 때
                if i == j[0]:
                    health -= j[1]
                    successCount = 0
                    # print(i, health, successCount)
                    break
    #           공격하는 시간이 아닐 때
                elif j[0] >= i:
                    print(j[0])
                    successCount += 1
                    if successCount == bandage[0]:
                        successCount = 0
                        health = health + bandage[1] + bandage[2]
                    else:
                        if(health != healthMaximum):
                            health += bandage[1]
                    # print(i, health, successCount)
                    if health > healthMaximum:
                        health = healthMaximum
                    break
                    
    answer = -1 if health <= 0 else health 
    return answer
