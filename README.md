# Random Password Generator

This is a simple Python script that generates a random password of a specified length. The generated password includes lowercase letters, uppercase letters, symbols, and digits.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or copy the script to your local machine.
2. Open the script using a text editor or an integrated development environment (IDE).
3. Run the script using a Python interpreter.
4. Follow the prompts to enter the desired password length.

## Explanation

1. The script begins by importing the necessary modules: `random` and `string`.
2. The welcome message is displayed to greet the user.
3. The `main()` function is defined to handle the password generation.
4. The user is prompted to enter the desired length of the password.
5. The `string` module is used to define four different character sets:
   - `lowerD`: lowercase letters
   - `upperD`: uppercase letters
   - `symbolD`: symbols/punctuation
   - `digitD`: digits
6. The four character sets are concatenated into the `combine` variable.
7. The `random.sample()` function is used to select random characters from the `combine` variable, based on the specified length.
8. The randomly selected characters are joined together to form the password using the `"".join()` function.
9. The generated password is printed to the console.
10. The `main()` function is called to start the password generation process.

Feel free to modify the script to suit your specific requirements or integrate it into your own projects. Enjoy generating random passwords!
