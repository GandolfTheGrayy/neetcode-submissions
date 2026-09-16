class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        str_size = 0

        for str in strs:
            str_size = len(str)
            encoded_string += f"{str_size}#{str}"
        return encoded_string 



    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

            
            
