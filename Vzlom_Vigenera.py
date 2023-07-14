
import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext = input("""Text: """)
    
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print('Копирование взломанного сообщения в буфер обмена:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Не удалось взломать шифрование')


def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()

    for word in words:
        word = word.strip() # Remove the newline at the end.
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found:
            print()
            print('Возможный ключ шифрования:')
            print('Ключ ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Нажмите D при нахождении ключа, либо Enter для продолжения перебора:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()
