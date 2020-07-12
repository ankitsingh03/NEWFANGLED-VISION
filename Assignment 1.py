input_str = '''“With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting 
the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud 
to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation” '''

validation_array = ["food", "face", "the", "donation", "coalition", "economy", "sector"]
validation_array = tuple(validation_array)


# method 1
for i in validation_array:
    count = 0
    index = 0
    while True:
        index = input_str.lower().find(i.lower(), index)
        if index != -1:
            count += 1
            index += 1
        else:
            break
    print(f"{i}: {count}")


# just to give space between two output
print()


# method 2
for j in validation_array:
    print(f"{j}: {input_str.lower().count(j.lower())}")
