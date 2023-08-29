class Solution:
    def decodeString(self, s: str) -> str:
        number = [f'{i}' for i in range(10)]
        i = 0
        while i < len(s):
            if s[i] in number:
                j = i
                while j < len(s):
                    if s[j] == '[':
                        break
                    j += 1
                num = int(s[i:j])
                l = j

                k = 0
                while j < len(s):
                    if s[j] == '[':
                        k += 1
                    if s[j] == ']':
                        if k == 1:
                            break
                        k -= 1
                    j += 1
                print(s[:i], " + ", s[l+1:j], " * ", f"{num}", " + ", s[j+1:], end=' = ')
                s = s[:i] + s[l+1:j] * num + s[j+1:]
                print(s)
            else:   
                i += 1
        return s