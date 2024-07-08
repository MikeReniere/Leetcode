class Solution:

    def isAnagram(s: str, t: str) -> bool:
            countS = {} # letter : number of instances
            countT = {} # two new hashmaps
            if len(s) != len(t): # if the lengths arent the same, then its guarenteed to be false
                return False
            for i in range(len(s)): # this counts the number of instances of each character and puts then in the hashamps
                countS[s[i]] = 1 + countS.get(s[i], 0) # get the key and add one to the count
                countT[t[i]] = 1 + countT.get(t[i], 0) # get the key 
            for c in countS:
                if countS[c] != countT.get(c,0):
                    return False
            return True

    a = isAnagram("anagram", "nagaram")
    print(a)
    