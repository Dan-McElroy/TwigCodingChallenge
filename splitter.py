def split_array(target_array, number_of_subs):
    """Splits an array into a number of
    equally-sized sub-arrays.
    
    Note: if the array does not divide
    evenly into the number of arrays
    given, the last sub-array will be 
    sized to the remainder of the division.
    
    :param target_array: The array to be
    split.
    :param number_of_subs: The number of
    sub-arrays to be produced.
    :returns: An array of sub-arrays
    evenly splitting the values from the
    input array.
    :raises TypeError: Raised if target_array
    is not a list, or number_of_subs is not
    an int.
    """
    
    #Check types of input
    if not isinstance(target_array, list):
        raise TypeError('target_array should be a list. Value provided was a ' 
        	+ type(target_array).__name__)
    if not isinstance(number_of_subs, int):
        raise TypeError('number_of_subs should be an int. Value provided was a ' 
        	+ type(number_of_subs).__name__)    
   
    # Check values of input
    if number_of_subs < 1:
        raise ValueError('Cannot create a non-positive number of sub-arrays.')
    
    # Use "ceiling division" to find the size for each sub-array 
    sub_length = -(-len(target_array) // number_of_subs)
       		   
    return [
        target_array[i*sub_length : (i+1)*sub_length] # Include a slice of the original array
        for i in range(number_of_subs) # For each sub-array
    ]
