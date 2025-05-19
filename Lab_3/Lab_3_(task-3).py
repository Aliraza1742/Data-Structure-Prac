import numpy as np

order = int(input('Enter the number of order'))
array1 = np.zeros((order, order))
array2 = np.zeros((order, order))

for_sum = np.zeros((order, order))  # this will be used in sum of matrix

for_right_diagonal = np.zeros((order, order))  # this will be used in the right diagonal sum matrix

for_left_diagonal = np.zeros((order, order))  # this will be used in the left diagonal sum matrix

product_of_matrix = np.zeros((order, order))


# function for adding the values in the matrix
def add_values(array):
    for i in range(order):
        for j in range(order):
            value = int(input('Enter Value'))
            array[i][j] = value
    print('One matrix completed')
    return array


# here i am calling the function for adding the values in both matrixes
add_values(array1)
add_values(array2)


def print_matrix(array):  # This function will print an array in matrix form
    for i in array:
        print(i)


print("Matrix 1 is :")
print_matrix(array1)

print("Matrix 2 is :")
print_matrix(array2)


def addition_of_matrix(array1, array2):
    for i in range(0, order):
        for j in range(0, order):
            summ = array1[i][j] + array2[i][j]
            for_sum[i][j] = summ

    print_matrix(for_sum)


print("The result of the addition of matrix is :")
addition_of_matrix(array1, array2)


def left_digonal_sum(array1, array2):
    for i in range(0, order):
        summ = array1[i][i] + array2[i][i]
        for_left_diagonal[i][i] = summ
    print_matrix(for_left_diagonal)


print("The result of the addition of left diagonal matrix is :")
left_digonal_sum(array1, array2)


# 2 way
def left_diagonal_sum(array1, array2):
    summ1 = 0
    summ2 = 0
    for i in range(0, order):
        summ1 = summ1 + array1[i][i]
        summ2 = summ2 + array2[i][i]
    print("The result of the sum of left diagonal of array1 is :", summ1)
    print("The result of the sum of left diagonal of array2 is :", summ2)


left_diagonal_sum(array1, array2)


def Right_diagonal_sum(array1, array2):
    j = order - 1
    for i in range(0, order):
        summ = array1[i][j] + array2[i][j]
        for_right_diagonal[i][j] = summ
        j -= 1

    print_matrix(for_right_diagonal)


print("The result of the addition of Right diagonal matrix is :")
Right_diagonal_sum(array1, array2)


# 2nd way
def Right_diagonal_sum(array1, array2):
    j = order - 1
    summ1 = 0
    summ2 = 0
    for i in range(0, order):
        summ1 = summ1 + array1[i][j]
        summ2 = summ2 + array2[i][j]
        j -= 1

    print("The result of the sum of Right diagonal of array1 is :", summ1)
    print("The result of the sum of Right diagonal of array2 is :", summ2)


Right_diagonal_sum(array1, array2)


def Average_of_matrix(array1, array2):
    sum_of_array1 = 0
    sum_of_array2 = 0

    for i in range(0, order):
        for j in range(0, order):
            sum_of_array1 = sum_of_array1 + array1[i][j]
            sum_of_array2 = sum_of_array2 + array2[i][j]
    Average_of_array1 = sum_of_array1 // 4
    Average_of_array2 = sum_of_array2 // 4

    print("The average of array1 is :", Average_of_array1)
    print(" The average of array2 is :", Average_of_array2)


Average_of_matrix(array1, array2)


def Multiplication_of_matrix(array1, array2):
    for i in range(0, 2):
        for j in range(0,
                       2):  # this j additional loop will be helpful in                        multiplying of array1 with the array 2
            sum = 0
            for k in range(0, 2):
                prod = array1[i][k] * array2[k][j]
                sum += prod
                product_of_matrix[i][j] = sum

    print_matrix(product_of_matrix)


print("The result of the Multipliction of 2 matrix is : ")
Multiplication_of_matrix(array1, array2)
