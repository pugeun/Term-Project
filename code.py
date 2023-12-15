import cv2
import numpy as np

def find_contours(frame):

def find_hand_contour(frame):
    contours = find_contours(frame)

    # 손의 윤곽 중 가장 큰 것 선택
    max_contour = max(contours, key=cv2.contourArea, default=None)

    return max_contour

def get_hand_gesture(approx):
    
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
