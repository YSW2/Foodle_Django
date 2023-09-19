import cv2
import pyzbar.pyzbar as pyzbar


def scanning():
    scanned_codes = set()
    cap = cv2.VideoCapture(0)
    my_code = None

    while cv2.waitKey(33) < 0:
        success, frame = cap.read()

        if success:
            for code in pyzbar.decode(frame):
                my_code = code.data.decode('utf-8')

                # 이미 스캔한 바코드인지 확인
                if my_code not in scanned_codes:
                    print("인식 성공: ", my_code)
                    scanned_codes.add(my_code)  # 스캔한 바코드를 집합에 추가
            cv2.imshow('cam', frame)

        if my_code is not None:
            break


    cap.release()
    cv2.destroyAllWindows()
    return my_code