# LL1Parser
Add LL1Parser class for parsing input string

The commit adds the LL1Parser class which implements a LL(1) parser for a given grammar. The LL1Parser class includes methods for creating a table, printing the parsing table, and parsing an input string based on the provided grammar and parsing rules. The commit also includes example usage of the LL1Parser class to parse an input string.

Changes Made:
- Added the LL1Parser class with its methods for table creation, printing, and parsing.
- Implemented the parse() method to perform LL(1) parsing of the input string.
- Created the create_table() and print_table() methods for displaying the parsing process.
- Added global variables DERIVATION, BUFFER, and OUTPUT to store the parsing details.
- Updated the example usage to parse an input string and display the parsing table.

Fixes #<issue_number>
