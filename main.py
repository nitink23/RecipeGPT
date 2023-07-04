import os
import streamlit as st
from langchain.llms import OpenAI
from apikey import apikey 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



os.environ['OPENAI_API_KEY'] = apikey
#APP framework
st.title('🍛RecipeGPT🍛')
prompt = st.text_input('Type in the curry you want to make and see the magic happen and there is a bonus at the bottom of the answer.')


#prompt template
ingredient_template = PromptTemplate(
  input_variables = ['ingredient'],
  template = 'list out in bullet points with a line in between the ingredients needed to make {ingredient}'
  
)


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

ingredient_chain = LLMChain(llm = lm, prompt = ingredient_template ,verbose = True)
spicy_chain = LLMChain(llm = lm,prompt = spicy_template,verbose = True)
curry_chain = LLMChain(llm = lm,prompt = curry_template, verbose = True)
video_chain = LLMChain(llm = lm,prompt = video_template, verbose = True)

# gives out a response
if prompt:
  response1 = curry_chain.run(prompt)
  response2 = spicy_chain.run(prompt)
  
  response4 = ingredient_chain.run(prompt)
  st.write('The ingredients to make this dish are:-')
  st.write(response4)
  st.write('The steps of preparation')
  st.write(response1)
  st.write('The ingredient that controls the spice level: ')
  st.write(response2)