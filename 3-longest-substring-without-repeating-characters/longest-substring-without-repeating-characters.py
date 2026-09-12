class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # stores the last seen index of each character
        start = 0        # left edge of the window
        max_len = 0
        
        for end in range(len(s)):
            char = s[end]
            
            # if this char was seen before AND it's inside our current window,
            # move the start pointer past its last occurrence
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            char_index[char] = end
            
            # current window size is end - start + 1
            max_len = max(max_len, end - start + 1)
        
        return max_len