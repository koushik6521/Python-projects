height = input ("enter height with spaces:\n")

heights = height.split() #here the inputs are divided and stored in heights

# better to use sum() fuction than for loop

total_heights = 0
for height in heights :
    total_heights = total_heights + int (height)
print (total_heights)


# better to use len() than for loop


total_num_heights = 0
for height in heights :
    total_num_heights = total_num_heights + 1
print (total_num_heights)

avg_height = round(total_heights / total_num_heights)

print (avg_height)