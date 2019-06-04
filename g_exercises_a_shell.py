# Name: ALEXIS ECHANO       Date: 2/11/2019   Version:
# Teacher: KIM     Period: 7
import sys
idx = int(sys.argv[1])-31

myRegexList = [
   r"/^0$|^10[10]$/",
   r"/^[01]*$/",
   r"/^[01]*0$/",
   r"/\w*[aeiou]\w*[aeiou]\w*/i",
   r"/^0$|^1[10]*0$/",
   r"/^[10]*110[10]*$/",
   r"/^\w{2,4}$/s",
   r"/^\d{3}\s*-?\s*\d{2}\s*-?\s*\d{4}$/",
   r"/^\w*?d/im",
   r"/^1*$|^0*$|^0[01]*0$|^1[01]*1$/",
   r"/^[.ox]{64}$/i",  # 41 starts here
   r"/^[ox]*\\w[ox]*$/i",
   r"/^\\w+\w*|\\w+$|^x+o*\\w|\\wo*x+$/i",
   r"/^\w(\w\w)*$/s",
   r"/^0([01]{2})*$|^1[01]$/",
   r"/\w*((a[eiou])|(e[aiou])|(i[eaou])|(o[eiau])|(u[eioa]))\w*/i",
   r"/^0*$|^1*$|^(0|10)*1*$/",
   r"/^[bc]+$|^[bc]*a[bc]*$/",
   r"/^[bc]+$|^(([bc]*a[bc]*){2})+$/",
   r"/^(2|1[20]*1)(([02]*1[02]*){2})*[02]*$/",
   r"/\(\w)+\w*\1/i",  # 51 starts here
   r"/(\w)+(\w*\1){3}/i",
   r"/^1*$|^0*$|^(0|1)[01]*\1$/",
   r"/(?=\w*(cat))\b\w{6}\b/i",
   r"/(?=\w*(bri))(?=\w*(ing))\b\w{5,9}\b/i",
   r"/(?!\w*(cat))\b\w{6}\b/i",
   r"/(?!\w*(\w)\w*\1)\b\w+\b/i",
   r"/^(?![01]*(10011))[01]*$/", #/^(0|(?!1001)1)*$/
   r"/\w*([aeiou])(?!\1)[aeiou]\w*/i",
   r"/^(?![01]*(1[01]1))[01]*$/",
   r"",  # 61 starts here
   r"",
   r"",
   r"",
   r"",
   r"",
   r"",
   r"",
   r"",
   r"",
   r"/(?=(.)+(.*\1){3,})^.{6}$/im",  # 71 starts here    COUNT: 24
   r"/(?=(.*([aeiou])(?!.*\2)){5})^.{,8}$/im",# COUNT: 35
   r"/(?=([^aeiou]*[aeiou][^aeiou]*){5}\b)^\w{17,}$/im", #COUNT: 45
   r"/^(.)(.)(.).{3,}\3\2\1$/im",   #COUNT: 22
   r"/(?=(.)+\1+)^.{20,}$/im",   #COUNT: 19
   r"/(?=(.)+(.*\1){5})^\w{9,}$/im",    #SHORTEN!!!! COUNT: 25
   r"/(?=((.)+\2){3})^\w{13,}$/im", #COUNT: 24
   r"",  #78 NOPE
   r"",  #79 NOPE
   r"/(?!(.)+(.*\1){2,})^\w{18}$/im",  #COUNT: 26
   ]
print(myRegexList[idx])

#Hint for how to write each RegEx
#Sample answer to check a string is 'a': "/^a$/"
#Sample answer to check each line start with a word character: "/^\./m"

'''
X means syntax error
E means script error
T means time out
M means missing
D means no trailing /
O means bad option
I means invalid regular expression
P means shouldn't be doing this
N means internal error
r'\ makes no \\
'''
#/(?=(.*([aeiou])(?!.*\2)){5})^.{15,}$/im