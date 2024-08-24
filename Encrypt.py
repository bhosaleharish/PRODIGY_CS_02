# Python code for encryption
# take path of image as input
path = r"C:\Users\bhosa\Desktop\Cyber security\1700584259771.jpeg"
try:
    # taking encryption key as input
    key = int(input('Enter Key for encryption of Image: '))

    # print path of image file and encryption key
    print('The path of file: ', path)
    print('Note: Encryption key and Decryption key must be the same.')
    print('Key for Decryption: ', key)

    # open file for reading purpose
    with open(path, 'rb') as fin:
        # storing image data in variable "image"
        image = fin.read()

    # converting image into byte array to perform encryption easily on numeric data
    image = bytearray(image)
    
    # performing XOR operation on each value of bytearray
    for index, value in enumerate(image):
        image[index] = value ^ key

    # opening file for writing purpose
    with open(path, 'wb') as fout:
        # writing encrypted data in image
        fout.write(image)

    print('Encryption Done...')

except Exception as e:
    print(f'An error occurred: {e}')