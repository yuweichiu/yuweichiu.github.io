import os
filename = [
    "./assets/images/FPN_02and03.png",
    "./assets/images/FPN_01.png",
    "./assets/images/FPN_02and03.png",
    "./assets/images/FPN_04.png",
    "./assets/images/FPN_tb01.png",
    "./assets/images/FPN_05.png",
    "./assets/images/FPN_tb02.png",
    "./assets/images/FPN_tb03.png"
]
post_id = "p0010"

print("mkdir ./assets/images/{0:s}".format(post_id))
for fi in filename:
    fi_old = fi
    fi = fi.replace("/images", "/images/"+post_id)
    print("mv {0:s} {1:s}".format(fi_old, fi))
