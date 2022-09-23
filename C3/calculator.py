
class Calculator:
    def eval(self, expression):
        ''' Insert your code to process the string input here '''
        # Accepts a STRING
        # Number, (spaces), addition, (spaces), number
        # Accept: "2+2", "2 * 2" <-- text error to user, "pineapple" <-- text error to user
        # Acceptable Inputs: "2 + 2", "2+2", "12 34 + 5 678" (read as 1234 + 5678), "2+++++++++++2" (read as 2 + 2), "2          ++++++++++ 3"
        # Unacceptable Inputs: "1234", "1234+", "+1234", "fghjekhgjrd"
        allowed_inputs = "0123456789+ "
        integer_one_string = ""
        integer_two_string = ""
        flag_integer_one_complete = False
        for char in expression:     
            if char not in allowed_inputs:  # Handling characters, other symbols (Ex. "*-=/asdaff")
                return "ERROR: Unexpected Input: " + char + ". Input must be alphanumeric and addition only! Ex \"3 + 2\""
            if char == '+':
                if len(integer_one_string) == 0:    # Handles no 1st integer (Ex. "+7328432")
                    return "ERROR: 1st integer not given!"
                flag_integer_one_complete = True
                if len(integer_two_string) > 0:    # Handles additional + when 2nd integer is being "read"
                    return "ERROR: Unexpected Input: " + char + ". Calculator can only add TWO integers!"
                continue    # Handles multiple +
            if char != ' ': # Handles unnecessary spaces ("111 222 + 333 444")
                if not flag_integer_one_complete: # add to 1st integer until first '+', then add to 2nd integer. 
                    integer_one_string += char
                else:   
                    integer_two_string += char
        if not flag_integer_one_complete:   # Handles No addition operator (Ex. "43243")
            return "ERROR: Addition operator not given!"
        if len(integer_two_string) == 0:    # Handles no 2nd integer, (Ex. "2432+   ")
            return "ERROR: 2nd integer not given!"
        
        result = int(integer_one_string) + int(integer_two_string)
        return result

    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            print(' = ', result)

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()