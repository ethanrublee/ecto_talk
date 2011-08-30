fname = 'webcam_circles.txt'
hl = [((_('(detect = [^\)]+\))', green, bold)),
       (_("(rgb2gray\['\w+'\])+", yellow)))]

after = r'Plasm\(\)'
until = 'if __name__'
