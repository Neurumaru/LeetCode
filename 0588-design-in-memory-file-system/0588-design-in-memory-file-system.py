from typing import List

def bisect(a: List[str], x: str, lo=0, hi=None, key=None):
    if hi == None:
        hi = len(a)
    if key == None:
        key = lambda x: x
    
    while lo < hi:
        mid = (lo + hi) // 2
        if key(a[mid]) < key(x): 
            lo = mid+1
        else: 
            hi = mid
    
    return lo

def insort(a: List[str], x: str, lo=0, hi=None, key=None):
    lo = bisect(a, x, lo, hi, key)
    if lo == len(a) or a[lo] != x:
        a.insert(lo, x)

class FileSystem:
    def __init__(self):
        self.path_list = []
        self.content_dict = {}

    def ls(self, path: str) -> List[str]:
        if path in self.content_dict:
            return [path.split('/')[-1]]

        if path == "/":
            path = ""

        index = bisect(self.path_list, path)
        result = []
        cache = ""
        for i in range(index, len(self.path_list)):
            if self.path_list[i].startswith(path + "/"):
                parse = self.path_list[i][len(path):]
                foldername = parse.split('/')[1]
                if foldername == cache:
                    continue
                cache = foldername
                result.append(cache)
            elif not self.path_list[i].startswith(path):
                break
        return result

    def mkdir(self, path: str) -> None:
        insort(self.path_list, path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        insort(self.path_list, filePath)
        self.content_dict.setdefault(filePath, "")
        self.content_dict[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.content_dict[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
null = None
input_list = []
output_list = []

Input = [
    ["FileSystem","ls","mkdir","ls"],
    [[],["/"],["/a/b/c"],["/a/b"]]
]
Output = [
    [null,[],null,["c"]]
]
input_list.append(Input)
output_list.append(Output)

Input = [
   ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"],
   [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
]
Output = [
    [null,[],null,null,["a"],"hello"]
]
input_list.append(Input)
output_list.append(Output)

Input = [
   ["FileSystem","ls","mkdir","mkdir","mkdir","ls","ls","mkdir","mkdir","mkdir","ls","ls","ls","ls","mkdir","mkdir","ls","ls","mkdir","mkdir","ls","ls","ls","mkdir","ls","mkdir","addContentToFile","addContentToFile","readContentFromFile","ls","addContentToFile","ls","addContentToFile","addContentToFile","ls","ls","addContentToFile","addContentToFile","ls","addContentToFile","addContentToFile","addContentToFile","ls","ls","ls","ls","addContentToFile"],
   [[],["/"],["/cee"],["/vlfoeytw"],["/fclgogby"],["/"],["/cee"],["/cee/yavvz"],["/psg"],["/a"],["/cee"],["/fclgogby"],["/fclgogby"],["/fclgogby"],["/z"],["/vlfoeytw/kkrk"],["/fclgogby"],["/"],["/vk"],["/ludtma"],["/ludtma"],["/cee/yavvz"],["/vlfoeytw/kkrk"],["/zrrdf"],["/"],["/yefch"],["/az","guogaqcr"],["/stanacta","zob"],["/stanacta"],["/yefch"],["/zrrdf/whrr","yf"],["/zrrdf/whrr"],["/eaj","pxqvdx"],["/jnbfqruc","ttbmvgx"],["/"],["/ludtma"],["/yefch/fyzi","eg"],["/cee/yavvz/oi","dodtsq"],["/"],["/glb","ipbj"],["/vlfoeytw/kkrk/ohlcjh","iqohkxt"],["/cv","tkhwu"],["/jnbfqruc"],["/cee/yavvz/oi"],["/a"],["/fclgogby"],["/kmwyer","nv"]]
]
Output = [
   [null,[],null,null,null,["cee","fclgogby","vlfoeytw"],[],null,null,null,["yavvz"],[],[],[],null,null,[],["a","cee","fclgogby","psg","vlfoeytw","z"],null,null,[],[],[],null,["a","cee","fclgogby","ludtma","psg","vk","vlfoeytw","z","zrrdf"],null,null,null,"zob",[],null,["whrr"],null,null,["a","az","cee","eaj","fclgogby","jnbfqruc","ludtma","psg","stanacta","vk","vlfoeytw","yefch","z","zrrdf"],[],null,null,["a","az","cee","eaj","fclgogby","jnbfqruc","ludtma","psg","stanacta","vk","vlfoeytw","yefch","z","zrrdf"],null,null,null,["jnbfqruc"],["oi"],[],[],null]
]
input_list.append(Input)
output_list.append(Output)


for i in range(len(input_list)):
    Input = input_list[i]
    Output = output_list[i]
    obj = FileSystem()
    for j, (op, param, expected) in enumerate(zip(Input[0][1:], Input[1][1:], Output[0][1:])):
        print(op, param)
        out = getattr(obj, op)(*param)
        print(out)
        if out != expected:
            print(f"Failed: {op} {param} | Expected: {expected} | Got: {out}")
            break