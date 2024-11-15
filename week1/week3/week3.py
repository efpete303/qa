#ask the user for the number of apples
print("How many apples should I remove ?")
apples_to_remove = int(input())
removed_apples = 0
#while loop to remove apples
while removed_apples < apples_to_remove:
    print(f"removed apples.{removed_apples}")
    removed_apples = removed_apples + 1
    # removed_apples += 1

