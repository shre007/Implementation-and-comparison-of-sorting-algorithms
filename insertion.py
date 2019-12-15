#Insertion_Sort
#Reference: https://www.youtube.com/watch?v=0GQRhOzUVRI&list=PLzgPDYo_3xunyLTJlmoH8IAUvet4-Ka0y&index=14
#Name: Shreyas Arvind Vaze
#Student ID: 1001649822

def InsertionSort(given_list) :
    for index in range(1, len(given_list)) :
        curr_value = given_list[index]
        position = index
        while curr_value<given_list[position-1] and position>0 :
            given_list[position] = given_list[position-1]
            position = position-1
        given_list[position] = curr_value

given_list = [2,4,3,5,1,7,6]
InsertionSort(given_list)
print(given_list)



