import pandas as pd
import random
import string

# قراءة ملف الإكسل
df = pd.read_excel("invites.xlsx")  # افترض أن العمود اسمه Name

# توليد كود رباعي فريد
def generate_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

# إنشاء روابط وصفحات
for index, row in df.iterrows():
    print(df.columns)
    name = row['Name']
    code = generate_code()
    
    # الرابط سيكون مثلاً على GitHub Pages أو Netlify
    link = f"https://mosabkassar.github.io/{code}.html"
    
    # إنشاء صفحة HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
      <meta charset="UTF-8">
      <title>دعوة</title>
      <style>
        body {{ font-family: Tahoma; text-align: center; margin-top: 50px; }}
        h1 {{ color: darkblue; }}
      </style>
    </head>
    <body>
      <h1>أهلا وسهلا يا {name}</h1>
      <p>نتمنى لك حفلة ممتعة 🎉</p>
    </body>
    </html>
    """
    
    # حفظ الصفحة باسم الكود
    with open(f"pages/{code}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"{name} → {code} → {link}")
