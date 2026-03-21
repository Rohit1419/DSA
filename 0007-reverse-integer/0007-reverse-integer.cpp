#include <climits>
class Solution {
public:
    int reverse(int x) {

        
        int reverseNum = 0;
        int ld = 0;

        bool isNegative = false;

        if(x<0){
            isNegative = true;
            x  =abs(x);
        }

        while(x>0){

            ld = x%10;
             if (reverseNum > INT_MAX / 10 || (reverseNum == INT_MAX / 10 && ld > 7)) {
            return 0;  
        }
        if (reverseNum < INT_MIN / 10 || (reverseNum == INT_MIN / 10 && ld < -8)) {
            return 0;  
        }

             reverseNum = (reverseNum *10) + ld;
           
           x= x/10;
            
        }

        if(isNegative){
            reverseNum  = - reverseNum;
        }

         return reverseNum;
        
    }
};