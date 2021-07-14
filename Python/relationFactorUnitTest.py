import math
#<!-- 1.0 = 30		0.32 = 25		0.1 = 20		0.032 = 15		0.01 = 10		0.0032 = 5 -->
#<!-- 1.0 = 30		0.316 = 25		0.1 = 20		0.0316 = 15		0.01 = 10		0.00316 = 5 -->
NUMFORMATTER = "{:5.8f}"
NUMFORMATTER_Mul = "{:5.4f}"

RelationFactorMul = 3 # Menu Input
# Bonus Input
RelationFriendshipFactor = 0.0 # Used also in Penalty Algorithm

# Penalty Input
RelationDislikeFactor = 0.00316
RepHit = 0.001 #RepBonus for Case 3

# New idea
# experimental variable
print("================== Start ===================")
UIControlValue = 15
X = (10**(UIControlValue /10))/1000
print("Control Value: " + NUMFORMATTER_Mul.format(X))

print("REPHIT ENTRY: " + NUMFORMATTER.format(RepHit))
# 10*log(1000*value)/log(10)
MaxUIvalue = 30 # better values for actual gameplay to make it more dynamic and changing will be in range 18-25
if RelationFriendshipFactor > 0:
    RelationFriendshipFactor = (10*math.log(1000*RelationFriendshipFactor)/math.log(10))/MaxUIvalue

RelationDislikeFactor = (10*math.log(1000*RelationDislikeFactor)/math.log(10))/MaxUIvalue


print("=====================================")
if RelationFriendshipFactor > 0:
    print("RelationFriendshipFactor UI value = " + NUMFORMATTER_Mul.format(RelationFriendshipFactor))
print("RelationDislikeFactor UI value = " + NUMFORMATTER_Mul.format(RelationDislikeFactor))

print("PENALTY Algorithm:")
print("=================== Important ==================")
print("REPHIT ENTRY: " + NUMFORMATTER.format(RepHit))
if RelationFriendshipFactor > 0:
    NewRepHit = RepHit * math.log(1.25 + (RelationFactorMul*RelationDislikeFactor*(RelationDislikeFactor/RelationFriendshipFactor)))
    print("Case 1, New RepHit = " + NUMFORMATTER.format(NewRepHit))
else:
    # Same as Bonus Case (Default Action)
    
    NewRepHit = RepHit*math.log(1.25 + (RelationFactorMul*RelationDislikeFactor*RelationDislikeFactor))
    print("Case 2, New RepHit = " + NUMFORMATTER.format(NewRepHit))


factor  = NewRepHit/RepHit
print("New value equals to "+ NUMFORMATTER_Mul.format(factor*100)+'%'+ " of the base value")

print("=================== END ==================")