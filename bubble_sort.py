def bubbleSort(array):

    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i -1):

            # compare two adjacent elements
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

numbers = [-3, 34, 0, 13, -7]
bubbleSort(numbers)

print('Sorted Array in Ascending order:')
print(numbers)
