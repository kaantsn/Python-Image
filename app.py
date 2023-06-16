import cv2

# Görüntüyü yükleme
image = cv2.imread('resim.jpg')

# Görüntüyü gri tonlamaya dönüştürme
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü ekranda gösterme
cv2.imshow('Gri Tonlamalı Görüntü', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
