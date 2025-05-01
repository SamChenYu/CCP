import sys
# python compiler.py 主程序.ccp

if __name__ == "__main__":
    # Check if file name is provided
    if len(sys.argv) < 2:
        print("Usage: python compiler.py <source_file>")
        sys.exit(1)

    # Init the keyword translation dictionary and the set of characters
    keyword_translation = {}
    chinese_chars = set()
    with open("translate.txt", "r", encoding="utf-8") as content:
        for line in content:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue
            split = line.split("->")
            keyword_translation[split[0]] = split[1]
            

            for i in range(len(split[0])):
                if split[0][i] not in chinese_chars:
                    chinese_chars.add(split[0][i])


    # Get source code from params
    source_file = sys.argv[1]
    
    with open(source_file, "r", encoding="utf-8") as content:
        translated_code = ""
        for line in content:
            if(line.startswith("#")):
                continue
            
            # Go through the keywords and replace them in the source code
            ptr = 0
            charBuffer = ""
            while(ptr < len(line)):
                if(chinese_chars.__contains__(line[ptr])):
                    charBuffer += line[ptr]
                elif(charBuffer in keyword_translation):
                    translated_code += keyword_translation[charBuffer]
                    translated_code += line[ptr]
                    charBuffer = ""
                else:
                    translated_code += line[ptr]
                ptr += 1
                

        #print(translated_code)
        exec(translated_code)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"