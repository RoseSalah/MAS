import gradio as gr
from model import chat_with_model

with gr.Blocks(css=".chat-container { display: flex; flex-direction: column; height: 100vh; }") as demo:
    gr.Markdown("# 📊 Market Analysis AI")
    chatbot = gr.Chatbot(label="Llama 3.2 Market Analyst", container=True)

    with gr.Row():
        user_input = gr.Textbox(show_label=False, placeholder="Type your message here...", lines=1, scale=9)
        submit_button = gr.Button("➤", elem_id="send-button", scale=1)
        clear_button = gr.Button("🗑", elem_id="clear-button", scale=1)

    def respond(user_input, history):
        history = history or []
        return chat_with_model(user_input, history), ""

    submit_button.click(fn=respond, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    user_input.submit(fn=respond, inputs=[user_input, chatbot], outputs=[chatbot, user_input])

    def clear_chat():
        return None

    clear_button.click(fn=clear_chat, inputs=[], outputs=chatbot)

demo.launch()
