class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 
        case  = abs(ord('a') - ord('A')) #Calculate the case difference in ASCII encoding, which is useful for case-insensitive comparisons or conversion between uppercase and lowercase letters.
        while left < right: #不用判断等于，因为等于的时候，一定是相等的。
            while left < right and self.not_letters_digits(s[left]): left += 1 #为什么要再判断一遍left和right的大小关系，是因为如果字符不符合要求，那么就需要移动指针，而指针如果一直移动就可能打破原有的大小关系
            while left < right and self.not_letters_digits(s[right]): right -= 1
            #小写变大写的写法
            s_l = ord(s[left]) - case if s[left] >= 'a' else ord(s[left]) #这里是要处理所有的小写字母，让他们减去（97-65）=32，转换为更小的大写字母对应的ASCII编码，来进行比较。所以这里又是把大小写的转换调过来了。
            s_r = ord(s[right]) - case if s[right] >= 'a' else ord(s[right])

            # 大写变小写的写法：
            # s_l = ord(s[left]) + case if s[left] < 'a' else ord(s[left])
            # s_r = ord(s[right]) + case if s[right] < 'a' else ord(s[right])
            if s_l != s_r: return False

            #移动指针
            left += 1
            right -= 1
        return True #为什么while跳出来之后的返回结果是True而不是False呢？。这涉及到算法的设计问题：
        # （1）要是这里设置为False，那么while里面就是要判断正反两个方向的每个字符是否相等，直到最后left == right了才能跳出来，这样的复杂度就是O(n)的。
        # （2）但是如果是设置为True，那么while循环内就只用判断是否存在不相等的字符，只要有，就说明不是回文字符串，就可以直接结束循环。这样的话，算法的时间复杂度<= O(n)。
        #所以未来涉及到while循环 + 返回布尔值的算法，可以考虑一下循环正常结束后，最终的返回是True还是Flase，然后倒推循环内应该如何进行判断。
    def not_letters_digits(self, c):
        return not 'A' <= c <= 'Z' and not 'a' <= c <= 'z' and not '0' <= c <= '9' #记住判断字母和数字的方式
    

solution = Solution()
s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
result = solution.isPalindrome(s)
print(result)