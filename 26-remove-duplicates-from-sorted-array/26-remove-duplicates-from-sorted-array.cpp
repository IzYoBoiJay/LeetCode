class Solution {
    
public:
    
    int removeDuplicates(vector<int>& nums) {
        
        /*
        Distance calculates the number of elements between
        the beginning of nums to the iterator returned by unique().
        The unique() function removes consecutive duplicates in the range,
        especially given that the array is in increasing order.
        */
        
        return distance(nums.begin(), unique( nums.begin(), nums.end() ) );
        
        //A two-pointer solution can be used here as well
        
    } //End function
    
}; //End class Solution