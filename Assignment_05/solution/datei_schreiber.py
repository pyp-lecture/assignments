f = open("ueber_mich.txt", "w")

f.write("Thomas\n")
f.write("Smits\n")
f.write("Mein Lieblingslied ist: Rocky motion picture theme song\n")
f.write("Ich esse gerne: Spaghetti Carbonara\n")

# Alternative
# text = [ "Thomas\n",
#          "Smits\n",
#          "Mein Lieblingslied ist: Rocky motion picture theme song\n",
#          "Ich esse gerne: Spaghetti Carbonara\n" ]
#
# f.writelines(text)

f.close()
