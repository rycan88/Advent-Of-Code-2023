inp = r'''%jr -> mq, xn
%zl -> tz, cm
&lh -> nr
%hx -> jx, tz
%cm -> tz, ls
&fk -> nr
broadcaster -> sj, pf, kh, cn
%gz -> mq, lq
%gb -> xf, kr
%zc -> rq
%ln -> qj, xf
%gq -> pp
%fb -> xf
%pf -> tg, nv
%bc -> cf
&tz -> cn, fk, ls
%cq -> fb, xf
%rq -> tg, dx
%km -> gq
&mq -> gq, xn, fv, km, lh, xv, sj
%zp -> mq, xv
%jx -> tz, np
&tg -> mm, rp, zc, pf, bc
%cv -> sq, xf
%nv -> ht, tg
%sq -> gb
%kr -> ln
%dk -> cv
%xn -> zp
%sx -> xf, cq
%zt -> tz, fq
%dx -> tg, qn
&ff -> nr
%bn -> hx, tz
%fj -> zt, tz
%ht -> rr, tg
%fq -> tz, bn
%kh -> dk, xf
%sj -> mq, fv
%vm -> zl, tz
&mm -> nr
%rp -> bc
%fh -> sx
%ls -> fj
%xz -> mq, gz
%fv -> km
&nr -> rx
%lq -> mq
%xv -> xz
%cn -> tz, vm
%pp -> jr, mq
%hn -> tg
%qn -> hn, tg
%rr -> rp, tg
%cf -> tg, zc
%qj -> fh, xf
&xf -> sq, dk, fh, ff, kh, kr
%np -> tz'''

'''
from collections import defaultdict

def sendSignal(name, is_high_signal):
    Box = []
    if name not in Sym:
        return Box
    sym = Sym[name]

    if sym == "%":
        if not is_high_signal:
            Values[name] = not Values[name]
            sig = Values[name]
            for dest in Dest[name]:
                Box.append((dest, sig))
                LastSignal[(dest, name)] = sig
        return Box
    elif sym == "&":
        signal = False
        for source in Input[name]:
            if LastSignal[(name, source)] == False:
                signal = True
                break
            
        for dest in Dest[name]:
            Box.append((dest, signal))
            LastSignal[(dest, name)] = signal
        return Box

L = inp.split("\n")

Dest = {}
Sym = {}
Input = defaultdict(list)
LastSignal = {}
Values = {} # True if on or high, False is off or low
for line in L:
    first, second = line.split(" -> ")
    if first == "broadcaster":
        sym = ""
        name = first
    else:
        sym = first[0]
        name = first[1:]

    Box = second.split(", ")
    
    Dest[name] = Box
    Sym[name] = sym
    for dest in Box:
        Input[dest].append(name)
        LastSignal[(dest, name)] = False
    Values[name] = False



high_count = 0
low_count = 0
for turns in range(1000):
    Current = []
    current = "broadcaster"
    for dest in Dest[current]:
        Current.append((dest, False))
    low_count += 1

    while len(Current) > 0:
        current = Current.pop(0)
        is_high_signal = current[1]
        if is_high_signal:
            high_count += 1
        else:
            low_count += 1
        Signals = sendSignal(*current)
        Current += Signals
    
print(low_count * high_count)
'''

from collections import defaultdict
import time

t1 = time.time()
def sendSignal(name, is_high_signal):
    Box = []
    if name not in Sym:
        return Box
    sym = Sym[name]

    if sym == "%":
        if not is_high_signal:
            Values[name] = not Values[name]
            sig = Values[name]
            for dest in Dest[name]:
                Box.append((dest, sig))
                LastSignal[(dest, name)] = sig
        return Box
    elif sym == "&":
        signal = False
        for source in Input[name]:
            if LastSignal[(name, source)] == False:
                signal = True
                break

        endingname = "rx"
        if name == endingname and signal == False:
            print(name, turns)

        for dest in Dest[name]:
            Box.append((dest, signal))
            LastSignal[(dest, name)] = signal
        return Box

def getSignal(name):
    if sym == "%":
        return Values[name] 
    elif sym == "&":
        for source in Input[name]:
            if LastSignal[(name, source)] == False:
                return True
        return False
    return False

L = inp.split("\n")

D = {}
Dest = {}
Sym = {}
Input = defaultdict(list)
LastSignal = {}
Values = {} # True if on or high, False is off or low
for line in L:
    first, second = line.split(" -> ")
    if first == "broadcaster":
        sym = ""
        name = first
    else:
        sym = first[0]
        name = first[1:]

    Box = second.split(", ")
    
    Dest[name] = Box
    Sym[name] = sym
    for dest in Box:
        Input[dest].append(name)
        LastSignal[(dest, name)] = False
    Values[name] = False
    D[name] = False

for x in Sym:
    if Sym[x] == "%":
        break
        print(x, Input[x])
turns = 0
found = False

Changes = defaultdict(list)
while found == False:
    turns += 1
    Current = []
    current = "broadcaster"
    for dest in Dest[current]:
        Current.append((dest, False))

    counter = 0
    while len(Current) > 0:
        counter += 1
        current = Current.pop(0)
        if current[0] == "rx":
            if not current[1]:
                found = True
                break
        Signals = sendSignal(*current)
        Current += Signals

    
    for name in Sym:
        sig = getSignal(name)
        sym = Sym[name]
        if D[name] != sig:
            Changes[(sym, name)].append(turns)
        D[name] = sig

    if turns == 20000000000:
        # for name in Changes:
        #     print(name, Changes[name][:10])
        break
    
print(turns)

print(time.time() - t1)

# LOW 113200000
# LOW 165000000
# 228282646835717

'''
lh, fk, ff, mm => nr

broadcaster -> sj, pf, kh, cn
%sj -> mq, fv [2t = 1, 2t + 1 = 0]
%pf -> tg, nv [2t = 1, 2t + 1 = 0]
%kh -> dk, xf [2t = 1, 2t + 1 = 0]
%cn -> tz, vm [2t = 1, 2t + 1 = 0]
----------------------------------------
&mq -> gq, xn, fv, km, lh, xv, sj
%fv -> km [4t = 1, 4t + 2 = 0]

&tg -> mm, rp, zc, pf, bc
%nv -> ht, tg [4t = 1, 4t + 2 = 0]

%dk -> cv [4t = 1, 4t + 2 = 0]
&xf -> sq, dk, fh, ff, kh, kr

&tz -> cn, fk, ls
%vm -> zl, tz [4t = 1, 4t + 2 = 0]
------------------------------------------
%km -> gq [8t = 1 8t + 4 = 0]

%ht -> rr, tg [8t = 1 8t + 4 = 0]

%cv -> sq, xf [8t = 1 8t + 4 = 0]

%zl -> tz, cm [8t = 1 8t + 4 = 0]
-------------------------------------------

%gq -> pp [16t = 1 16t + 8 = 0]

%rr -> rp, tg [16t = 1 16t + 8 = 0]

%sq -> gb [16t = 1 16t + 8 = 0]

%cm -> tz, ls [16t = 1 16t + 8 = 0]

------------------------------------

%pp -> jr, mq [32t = 1 32t + 16 = 0]
%rp -> bc
%gb -> xf, kr
%ls -> fj

--------------------------------------

%jr -> mq, xn [64t = 1 64t + 32 = 0]
%bc -> cf
%kr -> ln
%fj -> zt, tz

--------------------------------------

%xn -> zp [128t = 1 128t + 64 = 0]
%cf -> tg, zc
%ln -> qj, xf
%zt -> tz, fq

--------------------------------------
%zp -> mq, xv [256 = 1 256t + 128 = 0]
%zc -> rq
%qj -> fh, xf
%fq -> tz, bn
-----------------------------------
%xv -> xz [512t = 1 512t + 256 = 0]
%rq -> tg, dx
%fh -> sx
%bn -> hx, tz
----------------------------------
%xz -> mq, gz [1024t = 1 1024t + 512 = 0]
%dx -> tg, qn
%sx -> xf, cq
%hx -> jx, tz

------------------------------
%gz -> mq, lq [2048 = 1 2048t + 1024 = 0]
%qn -> hn, tg
%cq -> fb, xf
%jx -> tz, np
-----------------------------

%lq -> mq [4096t = 1 4096t + 2048 = 0]
%hn -> tg
%fb -> xf
%np -> tz
---------------------------

tz ['zl', 'hx', 'cm', 'jx', 'zt', 'bn', 'fj', 'fq', 'vm', 'cn', 'np']
mq ['jr', 'gz', 'zp', 'sj', 'xz', 'lq', 'pp']
tg ['pf', 'rq', 'nv', 'dx', 'ht', 'hn', 'qn', 'rr', 'cf']
xf ['gb', 'ln', 'fb', 'cq', 'cv', 'sx', 'kh', 'qj']
ff ['xf']
mm ['tg']
lh ['mq']
fk ['tz']
nr ['lh', 'fk', 'ff', 'mm']


[mq, tg, xf, tz]

('%', 'hx') [1, 256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304]
('%', 'pf') [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
('%', 'cq') [1, 512, 1024, 1536, 2048, 2560, 3072, 3584, 3797, 4309]
('%', 'zp') [1, 64, 128, 192, 256, 320, 384, 448, 512, 576]
('%', 'cv') [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]
('%', 'bn') [1, 128, 256, 384, 512, 640, 768, 896, 1024, 1152]
('%', 'kh') [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
('%', 'sj') [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
('%', 'rp') [1, 8, 16, 24, 32, 40, 48, 56, 64, 72]
('%', 'lq') [1, 1024, 2048, 3072, 3761, 4785, 5809, 6833, 7522, 8546]
('%', 'cn') [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
('%', 'np') [1, 1024, 2048, 3072, 4079, 5103, 6127, 7151, 8158, 9182]
('%', 'nv') [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
('%', 'dk') [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
('%', 'vm') [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
('%', 'fv') [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
('%', 'zl') [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
('%', 'km') [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
('%', 'ht') [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
('%', 'cm') [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
('%', 'gq') [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
('%', 'sq') [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
('%', 'rr') [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]
('%', 'gb') [16, 32, 48, 64, 80, 96, 112, 128, 144, 160]
('%', 'ls') [16, 32, 48, 64, 80, 96, 112, 128, 144, 160]
('%', 'pp') [16, 32, 48, 64, 80, 96, 112, 128, 144, 160]
('%', 'jr') [32, 64, 96, 128, 160, 192, 224, 256, 288, 320]
('%', 'bc') [32, 64, 96, 128, 160, 192, 224, 256, 288, 320]
('%', 'kr') [32, 64, 96, 128, 160, 192, 224, 256, 288, 320]
('%', 'fj') [32, 64, 96, 128, 160, 192, 224, 256, 288, 320]
('%', 'xn') [64, 128, 192, 256, 320, 384, 448, 512, 576, 640]
('%', 'zt') [64, 128, 192, 256, 320, 384, 448, 512, 576, 640]
('%', 'cf') [64, 128, 192, 256, 320, 384, 448, 512, 576, 640]
('%', 'zc') [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
('%', 'fq') [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
('%', 'qj') [128, 256, 384, 512, 640, 768, 896, 1024, 1152, 1280]
('%', 'rq') [256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560]
('%', 'fh') [256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560]
('%', 'xv') [256, 512, 768, 1024, 1280, 1536, 1792, 2048, 2304, 2560]
('%', 'sx') [512, 1024, 1536, 2048, 2560, 3072, 3584, 3797, 4309, 4821]
('%', 'dx') [512, 1024, 1536, 2048, 2560, 3072, 3584, 3919, 4431, 4943]
('%', 'jx') [1024, 2048, 3072, 4079, 5103, 6127, 7151, 8158, 9182, 10206]
('%', 'qn') [1024, 2048, 3072, 3919, 4943, 5967, 6991, 7838, 8862, 9886]
('%', 'fb') [2048, 3797, 5845, 7594, 9642, 11391, 13439, 15188, 17236, 18985]
('%', 'hn') [2048, 3919, 5967, 7838, 9886, 11757, 13805, 15676, 17724, 19595]'''

'''
lh ['mq']
fk ['tz']
tz ['zl', 'hx', 'cm', 'jx', 'zt', 'bn', 'fj', 'fq', 'vm', 'cn', 'np']
mq ['jr', 'gz', 'zp', 'sj', 'xz', 'lq', 'pp']
tg ['pf', 'rq', 'nv', 'dx', 'ht', 'hn', 'qn', 'rr', 'cf']
ff ['xf']
mm ['tg']
nr ['lh', 'fk', 'ff', 'mm']
xf ['gb', 'ln', 'fb', 'cq', 'cv', 'sx', 'kh', 'qj']'''

'''
jr ['pp']
zl ['vm']
hx ['bn']
cm ['zl']
gz ['xz']
gb ['sq']
zc ['tg', 'cf']
ln ['kr']
gq ['km', 'mq']
fb ['cq']
pf ['broadcaster', 'tg']
bc ['tg', 'rp']
cq ['sx']
rq ['zc']
km ['mq', 'fv']
zp ['xn']
jx ['hx']
cv ['dk']
nv ['pf']
sq ['cv', 'xf']
kr ['gb', 'xf']
dk ['kh', 'xf']
xn ['jr', 'mq']
sx ['fh']
zt ['fj']
dx ['rq']
bn ['fq']
fj ['ls']
ht ['nv']
fq ['zt']
kh ['broadcaster', 'xf']
vm ['cn']
rp ['tg', 'rr']
fh ['qj', 'xf']
ls ['cm', 'tz']
xz ['xv']
fv ['mq', 'sj']
lq ['gz']
xv ['mq', 'zp']
cn ['broadcaster', 'tz']
pp ['gq']
hn ['qn']
qn ['dx']
rr ['ht']
cf ['bc']
qj ['ln']
np ['jx']'''