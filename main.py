def create_table(index):
    table = []
    for _ in range(index):
        table.append(["", "", ""])
    return table


def print_table(table):
    col_width = 14

    print("+" + "-" * (col_width * 3 + 8) + "+")
    print(
        "| {:<{}} | {:<{}} | {:<{}} |".format(
            "  Derivation", col_width, "    Buffer", col_width, "    Output", col_width
        )
    )
    print("+" + "-" * (col_width * 3 + 8) + "+")

    for row in table:
        print(
            "| {:<{}} | {:<{}} | {:<{}} |".format(
                row[0], col_width, row[1], col_width, row[2], col_width
            )
        )

    print("+" + "-" * (col_width * 3 + 8) + "+")


# global
# to show data finally we define 3 arrays to keep data
DERIVATION = []
BUFFER = []
OUTPUT = []


class LL1Parser:
    # constrcutor
    def __init__(self):
        self.stack = []

        # a buffer that holds the input string
        self.buffer = ""

        # constant table
        self.table = {
            "E": {"d": 1, "(": 1},
            "E'": {"+": 2, ")": 3, "$": 3},
            "T": {"d": 4, "(": 4},
            "T'": {"+": 6, "*": 5, ")": 6, "$": 6},
            "F": {"d": 8, "(": 7},
        }
        # rules or grammar
        self.rules = {
            1: ["E", "-", ">", "T", "E'"],
            2: ["E'", "-", ">", "+", "T", "E'"],
            3: ["E'", "-", ">", "λ"],
            4: ["T", "-", ">", "F", "T'"],
            5: ["T'", "-", ">", "*", "F", "T'"],
            6: ["T'", "-", ">", "λ"],
            7: ["F", "-", ">", "(E)"],
            8: ["F'", "-", ">", "d"],
        }

    def reverse_rule(self, rule_arr):
        """a method for reversing rule that came from a stack"""

        # 1.reverse the rule array
        reverse_arr_rule = rule_arr[::-1]

        # an array to holds the each element of the revered array
        reverse_list = []

        # loopthrogh the reversed arr to add each element to a list
        # we done this because of ' sign it must include with its alphabet
        for char in reverse_arr_rule:
            # check > sign to break because we want the second part of the rule(first part of the revered rule)
            if char == ">":
                break
            else:
                reverse_list.append(char)

        return reverse_list

    def parse(self, input_string):
        """a method to parse the input string"""

        self.stack = ["$", "E"]

        # append a $ to buffer to start parsing
        self.buffer = input_string + "$"

        index = 0
        # loop until length of the stack equal to 0
        while len(self.stack) > 0:
            index += 1
            # add buffer to global buffer
            BUFFER.append(self.buffer)
            # get the top element in stack
            current_symbol = self.stack[-1]

            # get the first token of the input string
            current_token = self.buffer[0]

            # check for equality
            if current_symbol == current_token:
                # check for the final record and parsing process
                if current_symbol == current_token == "$":
                    # pop from stack , now stack is empty because it's final round
                    self.stack.pop()

                    # shift buffer for next element
                    self.buffer = self.buffer[1:]

                    # append Accept message to show
                    OUTPUT.append("Accept")

                    # append current_symbol for derivation
                    DERIVATION.append(current_symbol)

                else:
                    # pop from stack to check the next symbol
                    self.stack.pop()

                    # shift buffer for next element
                    self.buffer = self.buffer[1:]

                    # append POP message
                    OUTPUT.append("POP")

                    # append current_symbol for derivation
                    DERIVATION.append(current_symbol)

            # check for availability
            elif (
                current_symbol in self.table
                and current_token in self.table[current_symbol]
            ):
                # obtain rule(grammar) number from table
                rule_number = self.table[current_symbol][current_token]

                # add rule_number
                OUTPUT.append(rule_number)

                # obtain rule(grammar)
                rule = self.rules[rule_number]

                # call the reverse_rule method
                reverse_rule_arr = self.reverse_rule(rule)

                # pop from stack to check the next symbol
                self.stack.pop()

                # check for existence of λ
                if "λ" not in rule:
                    # extend the stack array with reverse_rule_arr
                    self.stack.extend(reverse_rule_arr)

                # add rule in DERIVATION
                DERIVATION.append("".join(rule))

            else:
                break

        # if stack is empty
        if self.stack:
            print("Input string is Invalid.")
        else:
            print("Input string is valid.")
            table = create_table(index)
            for i in range(index):
                # add data to table to show data
                record = [DERIVATION[i], BUFFER[i], OUTPUT[i]]
                table[i] = record
            print_table(table)


parser = LL1Parser()
input_string = "E"
parser.parse(input_string)
