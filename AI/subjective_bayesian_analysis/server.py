import gradio as gr 
from modules import shared, subjective_Bayesian

def create_SBA_interface():
    with gr.Row():
        with gr.Column():
            gr.Markdown("# Parameters")

            with gr.Row():
                with gr.Column():
                    gr.Markdown("$P(H|\lnot E)$")
                    SBA_P_H_not_E_slider = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5,label="Probability of Hypothesis given not Evidence")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("$P(H|E)$")
                    SBA_P_H_E_slider = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5,label="Probability of Hypothesis given Evidence")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("$P(H)$")
                    SBA_P_H_slider = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5,label="Probability of Hypothesis")

            with gr.Row():
                with gr.Column():
                    gr.Markdown("$P(E)$")
                    SBA_P_E_slider = gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5,label="Probability of Evidence")
            
                    gr.Markdown("$P(E|S)$")
                    SBA_P_E_S_textbox = gr.Textbox(label="Probability of Evidence given Subject",value="0.25",interactive=True)
                
            

            with gr.Row():
                with gr.Column():
                    SBA_clear_button = gr.Button("Clear",variant="secondary")
            
            with gr.Row():
                with gr.Column():
                    SBA_submit_button = gr.Button("Submit",variant="primary")

        with gr.Column():
            gr.Markdown("# Plot")
            gr.Markdown("$P(E|S) - P(H|S)$")
            SBA_plot = gr.Plot(label="Subjective Bayesian Analysis")

            gr.Markdown("# Result")
            gr.Markdown("$P(H|S)$")
            SBA_P_H_S_textbox = gr.Textbox(label="P(H|S)",value="0.5",interactive=False)

    # Methods
    SBA_parameter_list = [SBA_P_H_not_E_slider,SBA_P_H_E_slider,SBA_P_H_slider,SBA_P_E_S_textbox,SBA_P_E_slider,SBA_P_H_S_textbox]      
    SBA_clear_button.click(fn=subjective_Bayesian.clear_SBA_parameter,outputs=SBA_parameter_list)
    SBA_submit_button.click(fn=subjective_Bayesian.SBA_plot_and_calculate,inputs=SBA_parameter_list,outputs=[SBA_plot,SBA_P_H_S_textbox])


with gr.Blocks() as server:

    with gr.Tab("Subjective Bayesian Analysis"):
        create_SBA_interface()
    
    with gr.Tab("Help"):
        gr.Markdown("# Help")
        gr.Markdown("This project is build with gradio by Ruhao Tian.")

server.launch(share=True)

