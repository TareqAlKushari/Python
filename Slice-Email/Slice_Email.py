# ---------------------------
# -- Practical Slice Email --
# ---------------------------

name = input('What\'s Your Name ?').strip().capitalize()
email = input('What\'s Your Email ?').strip()

userName = email[:email.index("@")]
website = email[email.index("@") + 1:]

print(f"Hello {name} Your Email Is {email}")
print(f"Your Username Is {userName} \nand Your Website Is {website}")
