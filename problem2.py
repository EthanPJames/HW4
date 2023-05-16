def stencil(data, f, w):
    """
    1) perform a stencil using the filter function f with width, w, on list, data.
    2) return the resulting list output.
    3) note that if len(data) = k, len(output) = k - width + 1.
    4) f will accept as input a list of size w and return a single number.

    :param data: list
    :param f: function
    :param w: int
    :return output: list
    """
    # Fill in

    output = []
    for i in range(len(data) - w + 1):
        window = data[i:i+w] #iterates through
        output.append(f(window)) #Adjust the list with valus found 

    return(output)


def create_box(box):
    """
    1) This function takes in a list, box.
    The box_filter function defined below accepts a list L of length len(box) and returns a simple
    convolution of it with the list, box.

    2) The meaning of this box filter is as follows:
    for each element of input list L, multiply L[i] by box[len(box) - 1  - i],
    sum the results of all of these multiplications and return the sum.

    3) For a box of length 3, box_filter(L) should return:
      (box[2] * L[0] + box[1] * L[1] + box[0] * L[2]),
      similarly, for a box of length 4, box_filter should return:
      (box[3] * L[0] + box[2] * L[1] + box[1] * L[2] + box[0] * L[3])

    The function create_box returns the box_filter function, as well as the length
    of the input list box

    :param box: list
    :return box_filter: function, len(box): int
    """

    # Fill in
    width = len(box) #width length of list
    #print("Width: %d\n" % width)
    
    def box_filter(L):
        # Fill in
        
        if len(L) != width: #What should this check be
            print("Calling box filter with the wrong length list. Expected length of list should be %d." % width)
            return(0)
        
        added_val = 0 #Declare a variable
        for i in range(len(box)):
            added_val +=  box[len(box) - 1 - i] * L[i] #Create the slide, iterats through by by subtrating
        return added_val
    

    return box_filter, len(box)


if __name__ == '__main__':

    def mov_avg(L):
        return float(sum(L)) / 3

    def sum_sq(L):
        return sum([i**2 for i in L])

    data = [1, 3, 5, 7, -9, -9, 11, 13, 15, 17, 19]

    print(stencil(data, mov_avg, 3))
    
    print(stencil(data, sum_sq, 5))
    
    # note that this creates a moving average!
    box_f1, width1 = create_box([1.0 / 3, 1.0 / 3, 1.0 / 3])
    print(stencil(data, box_f1, width1))
    #print("Here3")
    box_f2, width2 = create_box([-0.5, 0, 0, 0.5])
    print(stencil(data, box_f2, width2))
    #print("Here4")
