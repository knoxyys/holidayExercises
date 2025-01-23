import os

sitename = input("Site name: ")
author = input("Author: ")
javaf = input("Do you want a folder for JavaScript? ")
cssf = input("Do you want a folder for CSS? ")

current_dir = os.getcwd()
site_dir = os.path.join(current_dir, f'{sitename}')
js = os.path.join(site_dir, 'js')
css = os.path.join(site_dir, 'css')

if not os.path.exists(site_dir):
    os.makedirs(site_dir)
print(f"Created ./{sitename}")

with open (f"{site_dir}/index.html", "w") as hi:
    print(f"<title>\n   {sitename}\n</title>\n\n<meta>\n    {author}\n</meta>", file=hi)
    print(f"Created ./index.html")

if javaf == 'y':
    if not os.path.exists(js):
        os.makedirs(js)
        print(f"Created ./{sitename}/js")

if cssf == 'y':
    if not os.path.exists(css):
        os.makedirs(css)
        print(f"Created ./{sitename}/css")