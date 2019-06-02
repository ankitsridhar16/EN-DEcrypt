print("\n-------------------------------------by v3n0m-------------------------------------")
iteration = 1
while iteration > 0:
    from hashlib import *
    op = {
        "md5": lambda a: md5(a.encode()).hexdigest(),
        "sha1": lambda b: sha1(b.encode()).hexdigest(),
        "sha256": lambda c: sha256(c.encode()).hexdigest(),
        "sha384": lambda d: sha384(d.encode()).hexdigest(),
        "sha512": lambda e: sha512(e.encode()).hexdigest()
    }
    opr = input("\n"+"# iteration "+ str(iteration) +"\nDo u wanna (Decrypt) or (Encrypt) ? : ")
    opr = opr.strip().title()
    while opr not in ["Encrypt","Decrypt"]:
        opr = input("Do u wanna (Decrypt) or (Encrypt) ? : ")
        opr = opr.strip().title()
    if opr == "Encrypt":
        hashtype = input("Entre hash type [[md5] [sha1] [sha256] [sha384] [sha512]] => ")
        hashtype = hashtype.strip().lower()
        while hashtype not in ["md5","sha1","sha256","sha384","sha512"]:
            hashtype = input("Entre hash type [[md5] [sha1] [sha256] [sha384] [sha512]] => ")
            hashtype = hashtype.strip().lower()
        word = input("Entre the word u wanna encrypt: ")
        word = word.strip()
        x = str("{} = {}".format(word,op[hashtype](str(word))))
        print("\n " + "-"*len(x) + "\n|" + x + "|\n " + "-"*len(x))
    if opr == "Decrypt":
        hashtype = input("Entre hash type [[md5] [sha1] [sha256] [sha384] [sha512]] => ")
        hashtype = hashtype.strip().lower()
        while hashtype not in ["md5", "sha1", "sha256", "sha384", "sha512"]:
            hashtype = input("Entre hash type [[md5] [sha1] [sha256] [sha384] [sha512]] => ")
            hashtype = hashtype.strip().lower()
        word = input("Entre the hash: ")
        with open("word_list", mode="r") as file:
            a = 1
            for line in file:
                line = line.strip()
                if op[hashtype](str(line)) == word:
                    line = str(line)
                    x = str("your password is: " + line)
                    print("\n " + "-"*len(x) + "\n|" + x + "|\n " + "-"*len(x))
                    a = 0
            if a == 1:
                x = "No Match :("
                print("\n " + "-"*len(x) + "\n|" + x + "|\n " + "-"*len(x) )
    iteration += 1