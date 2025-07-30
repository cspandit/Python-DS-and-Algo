"""Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the
alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z
would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""

def caesarCipher(s,k):
    decoded_string = ""
    for x in s:
        n = ord(x)
        #to handle lower alphabet
        if 97 <= n <= 122:
            n = ((n-97+k) %26) + 97
        # to handle higher alphabet
        if 65 <= n <= 90:
            n = ((n-65+k) %26) + 65
        decoded_string += chr(n)
    return decoded_string

sample = "abcdefghijklmnopqrstuvwxyz"
decoded = "defghijklmnopqrstuvwxyzabc"
if decoded == caesarCipher(sample,3):
    print("Success")
