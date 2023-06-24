class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        '''
        The players will play optimally --> Apply greedy algorithm
        The algorithm is the same for both, but Alice ALWAYS plays first.
        A piece is valid if it is surrounded by 2, which means that 'AAA' and 'BBB' are valid
        The minimum length of these strings are the length of 3, and two are taken out of consideration
        The edges are never valid, but the rules make it never considered anyways. Let's say N is no character.
        'NAA', 'AAN', 'NBB', 'BBN' imply the middle cannot be removed which are actually the edges. 
        '''
        
        #Keep track of each player's count
        aliceMoves = 0
        bobMoves = 0
        
        #Keep track of the consecutive count of pieces
        count = 0
        
        #Iterate through the pieces
        for piece in colors:
            
            #Count the number of Alice pieces that are consecutive
            if piece == 'A':
                
                count += 1
                
            #If they are not consecutive
            else:
                
                
                #Valid if surrounded by 2 neighbors as well as cant be the 2 edges (left + valid + right)
                if count >= 3:
                    
                    #Calculate the moves
                    aliceMoves += count - 2
                
                #Reset count
                count = 0
            
        #Check at the end for Alice
        if count >= 3:
            
            aliceMoves += count - 2
        
        count = 0
                
        #Iterate through the pieces
        for piece in colors:
            
            #Count the number of Bob pieces that are consecutive
            if piece == 'B':
                
                count += 1
              
            #If they are not consecutive
            else:
                
                #Valid if surrounded by 2 neighbors as well as cant be the 2 edges (left + valid + right)
                if count >= 3:
                    
                    #Calculate the moves
                    bobMoves += count - 2
                    
                #Reset count
                count = 0
                
        #Check at the end for Bob
        if count >= 3:
            
            bobMoves += count - 2
        
        count = 0
                
        #Winner has more turns, and since Alice goes first we return the boolean result of who has more turns
        return aliceMoves > bobMoves