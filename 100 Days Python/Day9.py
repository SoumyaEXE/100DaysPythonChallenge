print("GENERATION DETECTOR FROM BIRTHYEAR")
print("-------------------")
print()
year = int(input("What year you were born?: "))
if year >= 1925 and year <= 1946:
  print("You're From Tradionalists Era! The Forgotten Ones")
elif year >= 1947 and year <= 1964:
   print("You're From Baby Boomers Era! The Greatest Ones")
elif year >= 1965 and year <= 1981:
 print("You're From GenX Era! The Era Of Inventions")
elif year >= 1982 and year <= 1995:
 print("You're From Milenials Era! The Golden Ones")
elif year >= 1996 and year <= 2015:
 print("You're From Generation Z Era, Often Called as GenZ! The Modern Ones, But Not Good")
else:
  print("Enter Birth Year From 1925 To 2015")
