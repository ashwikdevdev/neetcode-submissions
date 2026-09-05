class Solution:

    def encode(self, strs: List[str]) -> str:
        # strs = ["Neet","code","love","you"]
        return "".join(f"{len(word)}#{word}" for word in strs)


    def decode(self, s: str) -> List[str]:
        # str = "5#Hello5#World"
        print(s)
        res = []
        i=0
        while i<len(s):
            j= s.find('#', i)
            if s[i:j].isdigit():
                length = int(s[i:j])
                
                print(i ,j)
                print(length)
                word = s[j+1:j+length+1]
                print(word)
                res.append(word)
                i=j+length+1
                print(i ,j)
            

        return res

            


