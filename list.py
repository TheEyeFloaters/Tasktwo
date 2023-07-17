import os
import cv2

video_directory = r'C:\Users\murat\PycharmProjects\pythonProject5\videos'
output_directory = r'C:\Users\murat\PycharmProjects\pythonProject5\located'

video_files = os.listdir(video_directory)
video_output = os.listdir(output_directory)

for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)

    # Videoyu aç
    video_capture = cv2.VideoCapture(video_path)

    # Videodan alınacak frame sayısı
    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # İnsan tespiti için OpenCV'nin CascadeClassifier'ını kullan
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Kaydedilecek klasörü oluştur
    output_folder_path = os.path.join(output_directory, video_file.split('.')[0])
    os.makedirs(output_folder_path, exist_ok=True)

    # Videonun her bir frame'ini kontrol et
    for frame_index in range(frame_count):
        # Frame'i oku
        ret, frame = video_capture.read()

        # İnsan tespiti için gray scale'e dönüştür
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Yüzleri tespit et
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Eğer en az bir yüz tespit edilirse
        if len(faces) > 0:
            # İlk tespit edilen yüzün koordinatlarını al
            x, y, w, h = faces[0]

            # Yüzü çevreleyen dikdörtgeni çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Yüzün merkez noktasını hesapla
            center_x = x + (w // 2)
            center_y = y + (h // 2)

            # Yüzün olduğu alana odaklanan ROI (Region of Interest) oluştur
            roi_width = 300
            roi_height = 300
            roi_x = center_x - (roi_width // 2)
            roi_y = center_y - (roi_height // 2)

            # ROI'yi sınırlarını kontrol et ve sınırlar dışındaysa sınırları ayarla
            if roi_x < 0:
                roi_x = 0
            if roi_y < 0:
                roi_y = 0
            if roi_x + roi_width > frame.shape[1]:
                roi_x = frame.shape[1] - roi_width
            if roi_y + roi_height > frame.shape[0]:
                roi_y = frame.shape[0] - roi_height

            # ROI'yi çiz
            cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (255, 0, 0), 2)

            # Frame'i kaydet
            output_frame_path = os.path.join(output_folder_path, f"frame_{frame_index}.jpg")
            cv2.imwrite(output_frame_path, frame)

    # Videoyu serbest bırak
    video_capture.release()
