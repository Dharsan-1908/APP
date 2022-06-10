from pyDatalog import pyDatalog

pyDatalog.create_terms('"Bear","Elephant","cat","big","small","brown","black","gray","size","colour","x","Dark"')
+size("Bear","big")
+size("Elephant","big")
+size("cat","small")
+colour("Bear","brown")
+colour("cat","black")
+colour("Elephant","gray")
Dark(x) <= (colour(x,"black"))
Dark(x) <= (colour(x,"brown"))

print(size(x,"big"))