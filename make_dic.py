from stof_regi import *
def make_dic(gg):
    def is_number(x):
        try:
            float(x)
            return True
        except ValueError:
            return False
    def upper(x):
        return x == x.upper()
    def last(x):
        return is_number(x[-1])
    def space(text):
        if(last(text) == False):
            text += "1"
        text += "  "
        splitted = list()
        number = ""
        m = ""
        for i in range(len(text)-1):
            if(is_number(text[i]) == False and upper(text[i]) == True):
                m += text[i]
                if(upper(text[i+1]) == False and is_number(text[i+1]) == False):
                    m += text[i+1]
                if(number == ""):
                    number = "1"
                splitted.append(number)
                splitted.append(m)
                number,m = "",""
            elif(is_number(text[i]) == True):
                number += text[i]
        del splitted[0], splitted[-1]

        return splitted
    res = space(gg)
    print(res)
    def dics(x):

        t = dict()
        y = len(x)-1
        i = 0
        
        while(i <y):
            if(x[i] in t):
                t[x[i]] += float(x[i+1])
                continue
            t[x[i]] = float(x[i+1])
            i += 2
        return t 
    final = dics(res)
    M = 0
    for i in final:
        M += (final[i] * float(masse[i]))
  
    return M
stof = "H247Cl"
a = make_dic(stof)
