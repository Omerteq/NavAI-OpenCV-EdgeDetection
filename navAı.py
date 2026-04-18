import cv2

cam = cv2.VideoCapture(0) 

if not cam.isOpened():
    print("Kamera açılamadı")
    exit()

while True:
    ret, frame = cam.read() 
    if not ret:
        print("veri yok")
        break
    frame = cv2.flip(frame, 1)

    gri_filitre = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kenar_algilama = cv2.Canny(gri_filitre, 190, 250)

    cv2.imshow("Camera", frame) 
    cv2.imshow("Kenar Algilama", kenar_algilama)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()