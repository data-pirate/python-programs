import copy


def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: compound list: list of permutation with each permuted item being represented by a list
    """
    
    # compoundList to be returned
    finalCompoundList = []
    
    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        
        # Recursive function call
        sub_compoundList = permute(rest_list)
        
        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:
            
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList
    
    
print(permute([0, 1, 2]))
# will print [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
