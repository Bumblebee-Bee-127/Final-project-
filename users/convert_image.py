import base64

def con_image(name):
    with open(f'{name}.png', 'rb') as img:
        im = base64.b64encode(img.read()).decode('utf-8')
        return im

def con_b(byte, new_name):
    decoded_img = open(f'static/img/{new_name}.png', 'wb')
    decoded_img.write(base64.b64decode(byte))
    decoded_img.close()
