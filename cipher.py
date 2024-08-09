#Caesar cipher with a right shift of 5
#below is a dictionary reflecting the alphabet shifted by 5
letter_dict = {'a' : 'f', 'b' : 'g', 'c' : 'h', 'd' : 'i', 'e' : 'j', 'f' : 'k', 'g' :'l', 'h' : 'm', 'i' : 'n', 'j' : 'o', 'k' : 'p', 'l' : 'q', 'm' : 'r', 'n' : 's', 'o' : 't', 'p' : 'u', 'q' : 'v', 'r' : 'w', 's' : 'x', 't' : 'y', 'u' : 'z', 'v' : 'a', 'w' : 'b', 'x' : 'c', 'y' : 'd', 'z' : 'e'}
#input the sentence, changing any upercase to lowercase to match the dictionary
user_sentence = str.lower(input('Write your sentence here:')) 
#in order to use the translate method, first need to set up a translation table for the dictionary
my_table = str.maketrans(letter_dict)
#new variable to contain translated text
translated_text = user_sentence.translate(my_table)
print(translated_text)

