letters_1_19 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
letters_20_90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

total = 0

for i in range(1, 1001):
    word = ""
    if i == 1000:
        word = "onethousand"
    else:
        last2 = i % 100
        if i >= 100:
            h = i // 100
            word += letters_1_19[h-1] + "hundred"
            if i % 100 != 0: word += "and"
            
        if last2 != 0:
            if last2 < 20:
                word += letters_1_19[last2 - 1]
            else:
                t = last2 // 10
                word += letters_20_90[t-2]
                o = i % 10
                if o != 0:
                    word += letters_1_19[o-1]
    
    print(word)     
    total += len(word)
         
print(total) 