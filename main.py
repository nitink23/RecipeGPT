import os
import sys
print(sys.path)

import streamlit as st
from langchain.llms import OpenAI
from apikey import apikey
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



os.environ['OPENAI_API_KEY'] = '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'
#APP framework
st.title('🍛CurryGPT🍛')
prompt = st.text_input('Type in the curry you want to make and see the magic happen and there is a bonus at the bottom of the answer.')


#prompt template
curry_template = PromptTemplate(
  input_variables = ['curry'],
  template = 'write how this {curry} is made step by step'
  
)
spicy_template = PromptTemplate(
  input_variables = ['level'],
  template = ' which ingredient in {level} controls the spicy level ?'
)

video_template = PromptTemplate(
  input_variables = ['video'],
  template = ' find a youtube video that will help me make {video}'
)


# make this an llm
lm = OpenAI(temperature = 0.9)

spicy_chain = LLMChain(llm = lm,prompt = spicy_template,verbose = True)
curry_chain = LLMChain(llm = lm,prompt = curry_template, verbose = True)
video_chain = LLMChain(llm = lm,prompt = video_template, verbose = True)

# gives out a response
if prompt:
  response1 = curry_chain.run(prompt)
  response2 = spicy_chain.run(prompt)
  response3 = video_chain.run(prompt)
  st.write(response1)
  st.write('The ingredient that controls the spice level: ')
  st.write(response2)
  st.write('here is a video to help you make it')
  st.write(response3)
