print('Project -  Crypto')

def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
#? put the last char to the first spot in the string 
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries - one for encryption and decryption
    # dict_e = zip(keys,values)
    # print(dict_e) <zip object at 0x102cf28c0>
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 

# OR create 1 and then flip 
    #dict_e = dict(zip(keys,values))
    #dict_d = {value:key for key, value in dict_e.items()}

#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg.capitalize()
# return result
# clean and beautify the code 

print(enigma_light())