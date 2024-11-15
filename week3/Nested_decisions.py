#Nested Decisions counting Dashes Between Markers
print("Please enter a sequence?")
sequence = input()

#ask the user the enter the marker character
print("Please enter the character fot the marker")
marker  = input()
#initialize variable to find markers
marker_positions = [] #empty list []
#loop to position markers
for index, char in enumerate(sequence):
    if char == marker:
        marker_positions.append(index)
        #check if there is atleast two markers
if len(marker_positions)>=2:
    first_marker = marker_positions[0]
    last_marker = marker_positions[-1] #[-1] = last marker on the list
     #count dashes btween two markers
    dash_count = 0
    for i in range(first_marker+1, last_marker):
        if sequence[i] == "-":
          dash_count +=1
                    #display the result
    print(f" The distance between the markers is {dash_count}.")
else:
        print("The distance between the markers is 0.")



