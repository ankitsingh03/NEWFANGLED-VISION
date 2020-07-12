Problem 1:

We have a string “input_str”, and input_str can be any alpha-numeric text with length of 10 to 10000. 

Example of input_str:
Input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative.”

We have another variable, an array of words called “validation_array”. It can have upto 1000 items. 

Example of validation_array:
Validation_array = [“food”, “face”, “donation”, “coalition”, “economy”, “sector”]

We need to identify and print the output that the items in “validation_array” are occurring how many times in input_str. 

Example:

input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation”

validation_array = [“food”, “face”, “the”, “donation”, “coalition”, “economy”, “sector”]

output:

food: 1
face: 1
the: 6
donation: 2
coalition: 1
economy: 1
sector: 1





Problem 2:

We have a variable input_array which can contain items with alphanumeric of upto 1000 characters. We have another array called rejected_items. We need a function which will filter input_array and exclude all the items from rejected_items. “Input_array” can contain upto 1000 items, and rejected_items can contain upto 100 items. 

Example:
Input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]

rejected_items=["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]

Example of output in above example:
"impolite", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "memorise", "present", "brake", "sand", "lip", "talk", "abashed", "box", "chop", "tenuous", "robin", "trees", "moor", "hunt", "old-fashioned"
