import ciphers

i = 0
while True:

    print("d - decryption")
    print("e - encryption")
    type_of_op = input()
    ciphers_list = []

    # выбор операции шифровки/расшифровки
    # расшифровка
    if type_of_op == "d":
        print("Введите текст для расшифровки:")
        text_to_decrypt = input()
        print("Список доступных шифров:")
        print("1: Шифр цезаря")
        print("2: Шифр Атбаш")
        cipher_id = input()
        decrypted_stage = ""
        for id in cipher_id:
            if int(id) == 1:
                print("Сдвиг:")
                shift = int(input())
                decrypted_stage = ciphers.caesar_decrypt(text_to_decrypt, shift)
            if int(id) == 2:
                decrypted_stage = ciphers.atbash_decrypt(text_to_decrypt)
        print(decrypted_stage)
        print("=-=-=-=-=-=-=-=-=-=")
        print("Encrypted successfully")
        print("=-=-=-=-=-=-=-=-=-=")

        continue

    # шифровка

    if type_of_op == "e":
        print("Введите текст для зашифровки:")
        text_to_encrypt = input()
        print("Список доступных шифров:")
        print("1: Шифр цезаря")
        print("2: Шифр Атабаш")
        cipher_id = input()
        encrypted_stage = ""
        for id in cipher_id:
            if int(id) == 1:
                print("Сдвиг:")
                shift = int(input())
                encrypted_stage = ciphers.caesar_encrypt(text_to_encrypt, shift)
                text_to_encrypt = encrypted_stage
            if int(id) == 2:
                encrypted_stage = ciphers.atbash_encrypt(text_to_encrypt)
                text_to_encrypt = encrypted_stage
        print(encrypted_stage)
        print("=-=-=-=-=-=-=-=-=-=")
        print("Encrypted successfully")
        print("=-=-=-=-=-=-=-=-=-=")
        continue
