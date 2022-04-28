import streamlit as st
import streamlit.components.v1 as components

html_string = '''
<html>
  <head>
    <style>
        .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        }

        .button1 {width: 250px;}
        .button2 {width: 50%;}
        .button3 {width: 100%;}
        </style>
  </head>
  <p>
    <button type="button" id="record" class="button button1">Record</button>
    <button type="button" id="stopRecord" class="button button2">Stop</button>
  </p>
  <p>
    <audio id=recordedAudio></audio>        
  </p>

  <script> 
    navigator.mediaDevices.getUserMedia({audio:true})
    .then(stream => {handlerFunction(stream)})

    function handlerFunction(stream) {
      rec = new MediaRecorder(stream);
      rec.ondataavailable = e => {
        audioChunks.push(e.data);
        if (rec.state == "inactive"){
          let blob = new Blob(audioChunks,{type:'audio/mp3'});
          recordedAudio.src = URL.createObjectURL(blob);
          recordedAudio.controls=false;
          recordedAudio.autoplay=false;
          sendData(blob)
          }
        }
      }
    
    function sendData(data) {}
      record.onclick = e => {
        record.disabled = true;
        record.style.backgroundColor = "blue"
        stopRecord.disabled=false;
        audioChunks = [];
        rec.start();
        }
      stopRecord.onclick = e => {
        record.disabled = false;
        stop.disabled=true;
        record.style.backgroundColor = "red"
        rec.stop();
        }
  </script>
</html>
'''


def app():
    st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: rgb(204, 49, 49);
                    height: 5em;
                    width: 10em; 
                }
                </style>""", unsafe_allow_html=True)
    x = st.sidebar.expander("Description")
    x.write("test\ndfsdddddddddddddddddddddd\ndddddddddddddddddddddddddddd\nddddddddddddddddddddddd\ndddddddddddddddddddd\ndddddddddddddddddddddddddddfs")
    st.text_input("Enter you Name", help="this is your help" , key="1")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("Standard Pronunciation 🔊", key="1" )

    with c2:
        st.button("Custom Pronunciation 🔊", key="2")


