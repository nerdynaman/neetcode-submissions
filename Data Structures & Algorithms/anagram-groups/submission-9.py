class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {}
        for i in strs:
            sortedStr = ''.join(sorted(i))
            if sortedStr in output:
                output[sortedStr].append(i) 
            else:
                output[sortedStr] = [i]

        result = []
        for key, value in output.items():
            result.append(value)
        return result