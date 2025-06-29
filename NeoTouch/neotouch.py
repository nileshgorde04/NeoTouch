import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math

wScr, hScr = pyautogui.size()

mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_detection
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
face_detection = mp_face.FaceDetection(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
neutral_face_height = None
zoomed_in = False

def get_distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_hands = hands.process(img_rgb)
    result_face = face_detection.process(img_rgb)

    h, w, _ = img.shape
    lmList = []

    # --- Face Zoom Handling ---
    if result_face.detections:
        for detection in result_face.detections:
            bboxC = detection.location_data.relative_bounding_box
            face_height = bboxC.height * h

            if not neutral_face_height:
                neutral_face_height = face_height

            # Zoom In: when face gets close enough
            if face_height > neutral_face_height * 1.15 and not zoomed_in:
                pyautogui.hotkey('ctrl', '+')
                zoomed_in = True

            # Zoom Out: when face returns to near-neutral
            elif face_height < neutral_face_height * 1.05 and zoomed_in:
                pyautogui.hotkey('ctrl', '0')
                zoomed_in = False

    # --- Hand Gesture Control ---
    if result_hands.multi_hand_landmarks:
        for handLms in result_hands.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

        if lmList:
            x1, y1 = lmList[8]   # Index finger tip
            x2, y2 = lmList[4]   # Thumb tip
            x3, y3 = lmList[12]  # Middle finger tip

            # Move cursor with index finger
            screen_x = np.interp(x1, [0, w], [0, wScr])
            screen_y = np.interp(y1, [0, h], [0, hScr])
            pyautogui.moveTo(screen_x, screen_y, duration=0.1)

            # Click with pinch
            if get_distance((x1, y1), (x2, y2)) < 40:
                pyautogui.click()
                cv2.putText(img, 'Click!', (x1, y1-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Scroll: index + middle finger vertical gap
            scroll_distance = get_distance((x1, y1), (x3, y3))
            if scroll_distance < 50:
                if y1 < y3 - 20:
                    pyautogui.scroll(20)
                elif y1 > y3 + 20:
                    pyautogui.scroll(-20)

    cv2.imshow("Touchless Desktop Controller", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
