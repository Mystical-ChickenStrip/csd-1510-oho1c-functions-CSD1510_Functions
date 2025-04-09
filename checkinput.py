#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def check_input(prompt, error_message):
  """
  Prompts the user to enter an integer until a valid integer is provided.

  Args:
    prompt: The message to display to the user as a prompt.
    error_message: The message to display if the user enters non-integer input.

  Returns:
    The integer value entered by the user.
  """
  while True:
    user_input = input(prompt)
    try:
      integer_value = int(user_input)
      return integer_value  # Exit the loop if conversion is successful
    except ValueError:
      print(error_message)

# Supporting code to call the function and display the result
if __name__ == "__main__":
  input_number = check_input("Please enter an integer: ", "Invalid input. Please enter a whole number.")
  print("You entered the integer:", input_number)

  another_number = check_input("Enter another integer: ", "That was not a valid integer. Try again.")
  print("The second integer you entered is:", another_number)