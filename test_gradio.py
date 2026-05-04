import gradio as gr

def greet(name):
    return f"Hello {name}!"

iface = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your Name"),
    outputs=gr.Textbox(label="Greeting"),
    title="Test App"
)

iface.launch(debug=True, server_name="127.0.0.1", server_port=7860)