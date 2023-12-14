import cv2
import numpy as np

def find_contours(frame):
    # 손의 윤곽을 찾기 위한 전처리
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    _, thresh = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def find_hand_contour(frame):
    contours = find_contours(frame)

    # 손의 윤곽 중 가장 큰 것 선택
    max_contour = max(contours, key=cv2.contourArea, default=None)

    return max_contour

def get_hand_gesture(approx):
    # 손 제스처를 식별
    if len(approx) == 4:
        return "Paper"
    elif len(approx) == 12:
        return "Scissors"
    elif len(approx) > 15:
        return "Rock"
    else:
        return "Unknown"

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hand_contour = find_hand_contour(frame)

        if hand_contour is not None:
            epsilon = 0.02 * cv2.arcLength(hand_contour, True)
            approx = cv2.approxPolyDP(hand_contour, epsilon, True)

            gesture = get_hand_gesture(approx)

            cv2.drawContours(frame, [hand_contour], 0, (0, 255, 0), 2)
            cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Hand Gesture Recognition', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
