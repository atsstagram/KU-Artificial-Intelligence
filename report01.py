import numpy as np

START = np.array([[3,1,2],[0,6,5],[7,4,8]])
GOAL = np.array([[0,1,2],[3,4,5],[6,7,8]])

# calculation for heuristics
# using Manhattan distance
def cal_h(tiles):
    sum=0
    for i in range(3):
        for j in range(3):
            search=tiles[i][j]
            if(search==0):
                continue
            count=0
            if(search!=GOAL[i][j]):
                true_index=np.where(search==GOAL)
                count+=abs(true_index[0]-i)+abs(true_index[1]-j)
            sum+=count
    return sum

print(cal_h(START))


