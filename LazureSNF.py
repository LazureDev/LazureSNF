import os
import openai
import gradio as gr

openai.api_key = os.getenv("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")

start_sequence = "\nAI :"
restart_sequence = "\nHuman :"

prompt = "\n\nHuman: Hello!\nAI : Hi!",

def openai_create(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  return response.choices[0].text


def conversation_history(input, history):
  history = history or []
  s = list(sum(history,()))
  s.append(input)
  inp = ' '.join(s)
  output = openai_create(inp)
  history.append((input, output))
  return history, history

blocks = gr.Blocks()

with blocks:
  chatbot = gr.Chatbot()
  message = gr.Textbox(placeholder=prompt)
  state = gr.state()
  submit = gr.Button("Click")
  submit.click(conversation_history, imputs=[message,state], outputs=[chatbot, state])

blocks.launch(debug=True)
