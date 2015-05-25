letters_1_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
letters_20_90 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

total = 0

for i in range(1, 1001):
    word = ""
    if i == 1000: 
        word = "onethousand"
    else:
        if i >= 100:
            word += letters_1_19[i//100] + "hundred"
            if i % 100 != 0: word += "and"
            
        if i % 100 != 0:
            if i % 100 < 20:
                word += letters_1_19[i % 100]
            else:
                word += letters_20_90[(i%100)//10 - 2] + letters_1_19[i%10]
    
    print(word)     
    total += len(word)
         
print(total) 