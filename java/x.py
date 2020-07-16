# import qrcode

# qr = qrcode.QRCode(version=1,border=1)
# qr.add_data('Abdul Saboor: 03359648486 \nMuhammad Mashood: 03129675450')
# qr.make(fit=True)
# img = qr.make_image(fill='black',back_color="white")
# img.save('saboor.png')

import sys 

# sys.stderr.write('Failed')

one = sys.argv[1]

print(int(one)+5)



