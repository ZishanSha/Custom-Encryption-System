def encrypt(plaintext):
    """
    Encrypts plaintext using XOR with rotating key based on position.
    
    Args:
        plaintext (str): The text to encrypt
        
    Returns:
        str: Encrypted text
    """
    encrypted = ""
    key = 42  # Base key
    
    for i in range(len(plaintext)):
        c = plaintext[i]
        
        # XOR with rotating key based on position
        rotating_key = (key + i) % 256
        encrypted_char = chr(ord(c) ^ rotating_key)
        
        encrypted += encrypted_char
    
    return encrypted


def decrypt(ciphertext):
    """
    Decrypts ciphertext using XOR with rotating key (XOR is its own inverse).
    
    Args:
        ciphertext (str): The encrypted text to decrypt
        
    Returns:
        str: Decrypted text
    """
    decrypted = ""
    key = 42  # Same base key
    
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        
        # XOR with the same rotating key (XOR is its own inverse)
        rotating_key = (key + i) % 256
        decrypted_char = chr(ord(c) ^ rotating_key)
        
        decrypted += decrypted_char
    
    return decrypted


def encrypt_file(input_filename, output_filename):
    """
    Reads a file, encrypts its content, and writes to output file.
    
    Args:
        input_filename (str): Name of file to encrypt
        output_filename (str): Name of output encrypted file
    """
    try:
        # Read entire file content
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            all_text = input_file.read()
        
        # Encrypt the content
        encrypted_text = encrypt(all_text)
        
        # Write encrypted content to output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(encrypted_text)
        
        print(f"File encrypted successfully!")
        print(f"Input: {input_filename}")
        print(f"Output: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Could not open input file '{input_filename}'")
    except IOError as e:
        print(f"Error: Could not create output file '{output_filename}'")
        print(f"Details: {e}")


def decrypt_file(input_filename, output_filename):
    """
    Reads an encrypted file, decrypts its content, and writes to output file.
    
    Args:
        input_filename (str): Name of encrypted file to decrypt
        output_filename (str): Name of output decrypted file
    """
    try:
        # Read entire encrypted file content
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            all_text = input_file.read()
        
        # Decrypt the content
        decrypted_text = decrypt(all_text)
        
        # Write decrypted content to output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(decrypted_text)
        
        print(f"File decrypted successfully!")
        print(f"Input: {input_filename}")
        print(f"Output: {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: Could not open input file '{input_filename}'")
    except IOError as e:
        print(f"Error: Could not create output file '{output_filename}'")
        print(f"Details: {e}")


def main():
    """
    Main function - displays menu and handles user interaction.
    """
    print("=" * 40)
    print("   Custom Encryption Program")
    print("=" * 40)
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    print("=" * 40)
    
    try:
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            input_file = input("Enter input file name: ")
            output_file = input("Enter output file name: ")
            encrypt_file(input_file, output_file)
            
        elif choice == 2:
            input_file = input("Enter input file name: ")
            output_file = input("Enter output file name: ")
            decrypt_file(input_file, output_file)
            
        elif choice == 3:
            print("Exiting program. Goodbye!")
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            
    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")


if __name__ == "__main__":
    main()
