class Solution:
    def isPalindrome(self, s: str) -> bool:
        alfabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        kalimat = [i for i in s.lower() if i in alfabet]
        s = ''.join(kalimat)
        if s == s[::-1]:
            return True
        else:
            return False
