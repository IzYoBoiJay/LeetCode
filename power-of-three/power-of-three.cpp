class Solution {
public:
    bool isPowerOfThree(int n) {
        
        //Base case: If n is less than 1
        if(n < 1) {
            
            return false;
            
        } //end if
        
        //Integer maximum: 2147483647
        // 3^19 < 2147483647 < 3^19
        
        //Assuming math.h is available for pow()
        
        //Return the boolean result of the comparison (Cast power and n as ints)
        return ( (int)pow(3, 19) % (int)n == 0) ;
        
    } //end isPowerOfThree => O(1) Time & Space Complexity
    
};