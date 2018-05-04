email_address = open('email.list')

for line in email_address:
    if not line.startswith('To'):
        continue
    x = line.split()
    z = x[3]
    y = z.split('@')
    print(y)