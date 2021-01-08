def gener(l):
    digits_counter = {el: l.count(el) for el in l}
    for el in l:
        if digits_counter[el] == 1:
            yield el

test_list = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]
print([el for el in gener(test_list)])