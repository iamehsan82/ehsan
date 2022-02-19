vazn=int(input("vazn khod ra vared konid"))
ghad=int(input("ghad khod ra vared konid"))
ghad2=ghad**2/10000
bmi=vazn/ghad2
if bmi>=18.5 and bmi<=24.5 :
    print("bmi shoma barabar ast ba =",(round(bmi),"vazn shoma dar halat matlob ast"))
bmi2=vazn/ghad2
if bmi2>24.5:
    print("bmi shoma barabar ast ba =",(round(bmi),"shoma ezafe vazn darid"))
bmi3=vazn/ghad2
if bmi3<18.5:
    print("bmi shoma barabar ast ba =",(round(bmi),("shoma kambod vazn darid")))
