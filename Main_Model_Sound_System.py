from re import M
from sre_constants import SUCCESS
from unittest import result
import cv2
import mediapipe as mp
import math 
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import streamlit as st

def object_detection_video():
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volRange = volume.GetVolumeRange()
        minVol = volRange[0]
        maxvol = volRange[1]

        mp_drawing_styles = mp.solutions.drawing_styles
        mpDraw = mp.solutions.drawing_utils
        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        cap = cv2.VideoCapture(0)
        while True:
            success , img = cap.read()
            results = hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
            
            if results.multi_hand_landmarks:
                for handLms in results .multi_hand_landmarks:
                    lmList = []
                    for id, lm in enumerate(handLms.landmark):
                        h,w,c = img.shape
                        cx,cy = int(lm.x*w) , int(lm.y*h)
                        lmList.append([id,cx,cy])
                        mpDraw.draw_landmarks(img, handLms , mpHands.HAND_CONNECTIONS)
            
                    if lmList:
                        x1,y1 = lmList[4][1] , lmList[4][2]
                        x2,y2 = lmList[8][1] , lmList[8][2]
                        cv2.circle(img,(x1,y1),15,(122,12,12),cv2.FILLED)
                        cv2.circle(img,(x2,y2),15,(122,12,12),cv2.FILLED)
                        cv2.line(img,(x1,y1),(x2,y2), (1,12,12),3)
                        length = math.hypot(x2-x1 , y2-y1)
                        print(length)                
                        vol = np.interp(length,[20,400], [minVol , maxvol])

                        volBar = np.interp(length , [20 ,200] , [400 ,150])
                        volPer = np.interp(length , [20 ,200] , [0 ,100])

                        volume.SetMasterVolumeLevel(vol,None)
                        cv2.rectangle(img , (50 ,150) , (85 , 400) ,(250,213,122) ,3)
                        cv2.rectangle(img , (50 , int(volBar)) , (85 ,400) ,(300, 231,23) ,cv2.FILLED)
                        cv2.putText(img , str(int(volPer)) , (40, 450) ,cv2.FONT_HERSHEY_PLAIN ,4 , (24,34,34) , 3)
                        # cv2.putText(img ,str(int(b_level)) , (140, 450) ,cv2.FONT_HERSHEY_PLAIN ,4 , (24,34,34) , 3)

            cv2.imshow("Image",img)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def main():
    st.markdown("<h1 style='text-align: center; color: black; margin:-80px'>Sound Control Using Hand Gestures</h1>", unsafe_allow_html=True)

    st.markdown(
        """
        <style>
            [data-testid="stSidebar][aria-expanded="true"] > div:first-child{
                width:350px
            }

            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
                width:350px
                margin-left=-350px
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title('Open CV Wireles Sound Project')
    st.sidebar.subheader('Side Parameters')

    app_mode = st.sidebar.selectbox('Choose the App Mode',['About App','Run On Video'])

    if app_mode == 'About App':
        st.markdown("<p style='text-align: center; color: black;'>In this application, we are creating an application using open CV and mediapipe to control the sound of the system.</p>", unsafe_allow_html=True)

    elif app_mode =='Run On Video':

        st.set_option('deprecation.showfileUploaderEncoding',False)

        use_webcam = st.sidebar.button('Use Webcam')
        record = st.sidebar.checkbox("Record Video")

        if record:
            st.checkbox("Recording",value=True)

        st.markdown(
        """
        <style>
            [data-testid="stSidebar][aria-expanded="true"] > div:first-child{
                width:350px
            }

            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
                width:350px
                margin-left=-350px
            }
        </style>
        """,
        unsafe_allow_html=True
        )

        st.markdown("## Output")
        if use_webcam:
            # st.video(object_detection_video)
            object_detection_video()

if __name__ == '__main__':
		main()	