class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        #The black-white pattern alternates on letter, in which it would start on white or black and end in the latter.
        #Since a string of coordinates is given to us, one could check for the char of the letter and convert the second
        #char as a number to then check for evenness or oddness depending on the pattern.

        if coordinates[0] in 'aceg':

            #White squares are even
            return (int(coordinates[1]) % 2 == 0)

        elif coordinates[0] in 'bdfh':

            #White squares are odd

            return (int(coordinates[1]) % 2 != 0)