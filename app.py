import streamlit as st

st.write("""
# Finding max input!

This app finds the maximun num among all the entered numbers.
""")
#Get Input

st.header('User Input Parameters')
value1 = st.number_input("Value-1",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)
value2 = st.number_input("Value-2",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)
value3 = st.number_input("Value-3",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)

# def user_input_features():
#     value1 = st.number_input("Value-1",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)
#     value2 = st.number_input("Value-2",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)
#     value3 = st.number_input("Value-3",min_value=-1.797e+308,max_value=1.797e+308,step=1.0)


def find_max(a,b,c):
  if a>b:
    if a>c:
      return a
    else:
      return c
  else:
    if b>c:
      return b
    else:
      return c

st.subheader('The maximum value of the all your inputs:')
st.write(find_max(value1,value2,value3))
