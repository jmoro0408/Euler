"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage."""

num_dict = {n: 0 for n in range(1000)}
num_dict[0] = 0  #''
num_dict[1] = 3  #'one'
num_dict[2] = 3  #'two'
num_dict[3] = 5  #'three'
num_dict[4] = 4  #'four'
num_dict[5] = 4  #'five'
num_dict[6] = 3  #'six'
num_dict[7] = 5  #'seven'
num_dict[8] = 5  #'eight'
num_dict[9] = 4  #'nine'
num_dict[10] = 3  #'ten'
num_dict[11] = 6  #'eleven'
num_dict[12] = 6  #'twelve'
num_dict[13] = 8  #'thirteen'
num_dict[14] = 8  #'fourteen'
num_dict[15] = 7  #'fifteen'
num_dict[16] = 7  #'sixteen'
num_dict[17] = 9  #'seventeen'
num_dict[18] = 8  #'eighteen'
num_dict[19] = 8  #'nineteen'
num_dict[20] = 6  #'twenty'
num_dict[30] = 6  #'thirty'
num_dict[40] = 5  #'forty'
num_dict[50] = 5  #'fifty'
num_dict[60] = 5  #'sixty'
num_dict[70] = 7  #'seventy'
num_dict[80] = 6  #'eighty'
num_dict[90] = 6  #'ninety'

print(num_dict)
