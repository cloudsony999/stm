import streamlit as st


st.title('Lets learn STREAMLIT!!!!')
st.write('Hello How are U Ahana and family???')

st.markdown('**Hello How are U Preetha and family???**')

st.markdown('# I am Streamlit ')

st.markdown('''
            1. Pen
            2. Pencil
            3. Computer
            ''')
st.markdown('''
            - Pen
            - Pencil
            - Computer
            ''')

st.title('Streamlit rocks :100: :umbrella_with_rain_drops:')

st.title(':green[Streamlit] :violet[rocks]')

st.subheader('Hello Pari!!!')

st.divider()

st.code("""
        //Hello world in java
        class A
        {
        public static void main(String args[])
        {
        System.out.println("HI Preetha\n");
        }
        }      
        
        """,language='java')

st.text('Hello Sayantani',help='I am your help....')


x=st.checkbox('click to activate')
if x:
    st.write('Hi Trisha!!!')

choice=st.radio('Male/Female',('Male','Female'))

if choice:
    st.write(f'your gender is:  **{choice}**')

z=st.selectbox('please select favourite languages',('java','sql','python','javascript','go'))


if z:
    st.write(f'the chosed language is: **{z}** ')


z=st.multiselect('please select favourite languages',('java','sql','python','javascript','go'))


if z:
    d=','
    m=d.join(z)
    st.write(f'the chosed language is: **{m}** ')










