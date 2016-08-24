from toontown.suit import SuitDNA
import types
from toontown.toonbase import TTLocalizer
from direct.showbase import PythonUtil
from otp.otpbase import OTPGlobals
PartsPerSuit = (17,
 14,
 12,
 10,
 17)
PartsPerSuitBitmasks = (131071,
 130175,
 56447,
 56411,
 131071)
AllBits = 131071
MinPartLoss = 2
MaxPartLoss = 4
MeritsPerLevel = ((100, #Flunky
  130,
  160,
  190,
  800),
 (160, #Pencil Pusher
  210,
  260,
  310,
  1300),
 (260, #Yesman
  340,
  420,
  500,
  2100), 
 (420, #Micromanager
  550,
  680,
  810,
  3400), 
 (680, #Downsizer
  890,
  1100,
  1310,
  5550),
 (1100, #Head Hunter
  1440,
  1780,
  2120,
  8900),
 (1780, #Corporate Raider
  2330,
  2880,
  3430,
  14400),
 (2880, #The Big Cheese
  3770,
  4660,
  5550,
  5550,
  23300,
  0),
 (60, #Bottom Feeder
  80,
  100,
  120,
  500),
 (100, #Bloodsucker
  130,
  160,
  190,
  800),
 (160, #Double Talker
  210,
  260,
  310,
  1300),
 (260, #Ambulance Chaser
  340,
  420,
  500,
  2100), 
 (420, #Back Stabber
  550,
  680,
  810,
  3400),
 (680, #Spin Doctor 
  890,
  1100,
  1310,
  5550),
 (1100, #Legal Eagle
  1440,
  1780,
  2120,
  8900),
 (1780, #Big Wig
  2330,
  2880,
  3430,
  1780,
  14400,
  0),
 (40, #Short Change
  50,
  60,
  70,
  300),
 (60, #Penny Pincher
  80,
  100,
  120,
  500),
 (100, #Tightwad
  130,
  160,
  190,
  800),
 (160, #Bean Counter
  210,
  260,
  310,
  1300),
 (260, #Number Cruncher
  340,
  420,
  500,
  2100),
 (420, #Money Bags
  550,
  680,
  810,
  3400),
 (680, #Loan Shark
  890,
  1100,
  1310,
  5550),
 (1100, #Robber Baron
  1440,
  1780,
  2120,
  1100,
  8900,
  0),
 (20, #Cold Caller
  30,
  40,
  50,
  200),
 (40, #Telemarketer
  50,
  60,
  70,
  300),
 (60, #Name Dropper
  80,
  100,
  120,
  500),
 (100, #Glad Hander
  130,
  160,
  190,
  800),
 (160, #Mover & Shaker
  210,
  260,
  310,
  1300),
 (260, #Two-Face
  340,
  420,
  500,
  2100),
 (420, #The Mingler
  550,
  680,
  810,
  3400),
 (680, #Mr. Hollywood
  890,
  1100,
  1310,
  890,
  5550,
  0),
 (160, #Con Artist
  210,
  260,
  310,
  1300),
 (260, #Connoisseur
  340,
  420,
  500,
  2100), 
 (420, #Magnate
  550,
  680,
  810,
  3400), 
 (680, #Proprietor
  890,
  1100,
  1310,
  5550),
 (1100, #Big Shot
  1440,
  1780,
  2120,
  8900),
 (1780, #Toxic Leader
  2330,
  2880,
  3430,
  14400),
 (2880, #Big Fish
  3770,
  4660,
  5550,
  23300,
 (5550, #Head Honcho
  8900,
  14400,
  23300,
  5550,
  30000,
  0)))             
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
upperTorso = torsoLeftShoulder
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper,
 rightLegUpper,
 torsoLeftShoulder,
 leftArmUpper,
 rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper,
 rightLegFoot + rightLegLower + rightLegUpper,
 torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder,
 leftArmHand + leftArmLower + leftArmUpper,
 rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = TTLocalizer.CogPartNames
SimplePartNameStrings = TTLocalizer.CogPartNamesSimple
PartsQueryNames = ({1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: PartNameStrings[6],
  128: PartNameStrings[7],
  256: PartNameStrings[8],
  512: PartNameStrings[9],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[13],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[16]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[2],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[5],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]})
suitTypes = PythonUtil.Enum(('NoSuit', 'NoMerits', 'FullSuit'))

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    if dept == 4:
        return 1
    needMask = PartsPerSuitBitmasks[dept] & PartsQueryMasks[partIndex]
    haveMask = parts[dept] & PartsQueryMasks[partIndex]
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        index += 1


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in xrange(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0

    return 1

def getTotalMerits(toon, index):
    from toontown.battle import SuitBattleGlobals
    if index == 4:
        return 0
    cogIndex = toon.cogTypes[index] + SuitDNA.suitsPerDept * index
    cogTypeStr = SuitDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, len(MeritsPerLevel[cogIndex]) - 1), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 40):
    sum = 0
    for shift in xrange(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)

    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1

    str = ''
    for i in xrange(0, len(array)):
        str = str + array[i]

    return str


def asNumber(bitstring):
    num = 0
    for i in xrange(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)

    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = SuitDNA.suitDepts.index(dept)
    return dept
