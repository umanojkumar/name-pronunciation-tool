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
    x = st.sidebar.expander("Description2")
    x.write("test\ndfsdddddddddddddddddddddd\ndddddddddddddddddddddddddddd\nddddddddddddddddddddddd\ndddddddddddddddddddd\ndddddddddddddddddddddddddddfs")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.write("")
        st.text_input("Enter you Name", help="this is your help" , key="1")
    
    with c2:
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(204, 49, 49);
            height: 5em;
            width: 5em; 
        }
        </style>""", unsafe_allow_html=True)
        b = st.button("test", key="1" )

    with c3:
        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: rgb(50, 60, 10);
            height: 5em;
            width: 5em; 
        }
        </style>""", unsafe_allow_html=True)
        b = st.button("test", key="2")

    with c4:
        components.html(html_string)
        st.components

    # a =  st.expander("St")
    # a.button("Sdf")
    # components.html(html_string)
    # st.components
