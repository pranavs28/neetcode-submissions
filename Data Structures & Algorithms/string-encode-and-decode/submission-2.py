class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for word in strs:
            final_string += str(len(word)) + '#' + word
        
        return final_string

    def decode(self, s: str) -> List[str]:
        result = []
        string = s

        while len(string) > 0:
            index = string.find('#')
            str_len = int(string[0:index])
            result.append(string[index + 1: index + 1 + str_len])

            string = string[index + 1 + str_len:]
        return result

