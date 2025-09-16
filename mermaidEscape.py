myString = input("Enter the payload: ")

replacementDictionary = {"<":"&lt;",
                         ">":"&gt;",
                         ",":"&comma;",
                         "=":"&equals;",
                         "{":"&lcub;",
                         "[":"&lsqb;",
                         "_":"&lowbar;",
                         "(":"&lpar;",
                         ")":"&rpar;",
                         "]":"&rsqb;",
                         "}":"&rcub;",
                         "'":"&apos;",
                         "~":"&tilde;",
                         "/":"&sol;",
                         ":":"&colon;",
                         "\"":"&quot;",
                         ".":"&period;",
                         "-":"&hyphen;"}

for key in replacementDictionary.keys():
    myString = myString.replace(key,replacementDictionary[key])

print("Output: " + myString)
