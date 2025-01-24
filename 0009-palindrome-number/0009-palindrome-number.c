#include <stdbool.h>

bool isPalindrome(int x) {
    // Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }
    
    int revertedNumber = 0;
    int original = x;
    
    while (x > revertedNumber) {
        revertedNumber = revertedNumber * 10 + x % 10;
        x /= 10;
    }
    
    // Check if the original number matches the reversed number
    // For odd-length numbers, ignore the middle digit by revertedNumber / 10
    return x == revertedNumber || x == revertedNumber / 10;
}