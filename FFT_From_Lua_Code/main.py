from fft import bestCut, fftClause, withinCut
from testFile import O
from num import Num
from sym import Sym
import sys, re
from rows import Data


def addRow(data, cells):
    tempRows = []    
    for i, use in data._use.items():
        if (use == True):
            x = cells[i]
            x = str(x)
            if ("?" not in x):
                if(data.nums.get(i, 0) != 0):
                    x = float(x)
                    data.nums.get(i).numInc(x)
                else:
                    data.syms.get(i).symInc(x)
            else:
                x = 0
            tempRows.append(x)
    data.rows.append(tempRows)


def lines(source):
    if source[-3:] in ["csv"]:
        with open(source) as fs:
            for line in fs:
                yield line


def rows(src):
    cache = []    
    for line in src:
        line = re.sub(r'([ \n\r\t]|#.*)', "", line)
        cache += [line]
        if len(line) > 0:
            if line[-1] != ",":
                line = ''.join(cache)
                cache = []
                yield line


def header(data, cells):
    for i, x in enumerate(cells):
        if "%?" not in x:
            data._use[i] = True
            data.name.append(x)
            if re.search(r"[<>$]", x):
                data.nums[i] = Num()
            else:
                data.syms[i] = Sym()

            if re.search(r"<", x):
                data.w[i] = -1
            elif re.search(r">", x):
                data.w[i] = 1
            elif re.search(r"!", x):
                data.clss = i
            else:
                data.indeps[i] = True
        else:
            data._use[i] = False




def printOutput(csvFilename):
    first = True
    data = Data()
    for x in rows(lines(csvFilename)):
        if (first):
            first = False
            header(data, x.split(","))
        else:
            addRow(data, x.split(","))            
    data.doms()
    print (" Fast & Frugal Tree : ")
    fft(data, 4, "if")

    
def fft(t, d, pre):
    if d<=0:
        return True
    if len(t.rows) < 4:
        return True
    cut = bestCut(t)
    fftClause(cut, t, pre)
    otherwise = Data()
    header(otherwise, t.name)
    for x in t.rows:
        if not withinCut(x[cut.col], cut.lo, cut.hi):
            addRow(otherwise, x)
    return fft(otherwise, d-1, "else")


@O.k
def test1():
  print("\n\nweatherLong.csv\n\n")
  printOutput("data/weatherLong.csv")

@O.k
def test2():  
  print("\n\nauto.csv\n\n")
  printOutput("data/auto.csv")
