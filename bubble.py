#Bubble_Sort
#Reference: https://www.youtube.com/watch?v=GPv7gNRR9W4&list=PLzgPDYo_3xunyLTJlmoH8IAUvet4-Ka0y&index=6
#Name: Shreyas Arvind Vaze
#Student ID: 1001649822

givenlist = [12,18,4,28,2]
print("unsorted list:", givenlist)

for j in range(len(givenlist)-1) :
    for i in range(len(givenlist)-1) :
        if givenlist[i] > givenlist[i+1] :
            givenlist[i], givenlist[i+1] = givenlist[i+1], givenlist[i]
            print(givenlist)
        else :
            print(givenlist)

print("sorted list: ", givenlist)
