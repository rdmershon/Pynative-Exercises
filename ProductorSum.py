
#function for multiplication or sum
def multiplication_sum(num1,num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    else:
        return num1 + num2
        
# first condition
result = multiplication_sum(500,600)
print("the result is", result)
