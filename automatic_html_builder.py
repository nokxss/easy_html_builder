def putALine():
    print("Put a line after? Y/N")
    aa = input()
    if len(aa) > 0:
        aa = aa[0]
        aa = str(aa)
        if 'y' in aa:
            return f.write('        <hr>\n')
        else:
            return f.write('\n')
        
    else:
        return ('\n')

print("Welcome to the Automatic HTML Creator!")
filename = input("Name of the file: ")
cssname = input("Name of the CSS file: ")
fST = "{}.html"
sST = "{}.css"
f = open(fST.format(filename), "w+")
css = open(sST.format(cssname), "w+")
sST = sST.format(cssname)
x = input("Title: ")
print("Choose features: \n 1 for <h1> \n 2 for <p> \n Q to stop choosing")
choise = True
h1_amount = 0
p_amount = 0
while choise:
    y = input()
    if y == "1":
        h1_amount+=1
    elif y == "2":
        p_amount+=1
    elif y == "Q" or "q":
        choise = False

f.write("<!DOCTYPE HTML>\n")
f.write('<html lang="pl-PL">\n')
f.write('    <head>\n')
f.write('        <meta charset="utf-8" />\n')
lST = '        <link rel="stylesheet" href="{}">\n'
f.write(lST.format(sST))
st = ('        <title> {} </title>\n')
f.write(st.format(x))
f.write('    </head>\n')
f.write('    <body>\n')
for i in range(h1_amount):
    h1 = '        <h1>{}</h1> <br />\n'
    z = input(str(i+1) + " h1 value: ")
    f.write(h1.format(z))
    putALine()
for k in range(p_amount):
    p = '        <p>{}</p> <br />\n'
    zz = input(str(k+1) + " p value: ")
    f.write(p.format(zz))
    putALine()
f.write('    </body>\n') 
f.write('</html>\n')
f.close()
css.close()
input("Press any key to continue... ")
#dodana funkcjonalność <body>
#dodana funkcjonalność dodawania niezliczonej ilości <h1> i <p>
#dodana funkcja tworzenia pliku o dowolnej nazwie + .html
