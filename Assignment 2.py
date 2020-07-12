Input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]

rejected_items = ["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]
rejected_items = tuple(rejected_items)

for i in rejected_items:
    while True:
        if i in Input_array:
            Input_array.remove(i)
        else:
            break

print(Input_array)
