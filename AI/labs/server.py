import gradio as gr
from modules import shared, subjective_Bayesian, eight_puzzle_problem

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

def create_EPP_interface():
    with gr.Row():
        with gr.Column():
            gr.Markdown("# Parameters")

            # choose algorithm
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Algorithm")
                    EPP_algorithm_dropdown = gr.Dropdown(shared.EPP_algorithm_list,label="Algorithm",value="BFS",interactive=True)
            
            # input 8 tile sequence
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Input Sequence")
                    gr.Markdown("Please type in the sequence of the 8 tiles, column wise first.\n\nThe numbers in tile ranged from 0 ~ 8, from which 0 means empty tile. \n\nFor Example: 123456780 = [[1,2,3],[4,5,6],[7,8,0]]")
                    EPP_input_sequence_textbox = gr.Textbox(label="Input Sequence",value="123456780",interactive=True)


            # input target 8 tile sequence
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Target Sequence")
                    gr.Markdown("Please type in the target sequence of the 8 tiles, column wise first.\n\nThe numbers in tile ranged from 0 ~ 8, from which 0 means empty tile. \n\nFor Example: 123456780 = [[1,2,3],[4,5,6],[7,8,0]]")
                    EPP_target_sequence_textbox = gr.Textbox(label="Target Sequence",value="123456780",interactive=True)
            
            # max step
            with gr.Row():
                with gr.Column():
                    gr.Markdown("## Max Step")
                    EPP_max_step_textbox = gr.Textbox(label="Max Step",value="10000",interactive=True)

            # submit button
            with gr.Row():
                with gr.Column():
                    EPP_submit_button = gr.Button("Submit",variant="primary")

        with gr.Column():
            gr.Markdown("# Output")

            # Status
            # Including: Solved, no solution, solving, invalid input
            with gr.Row():
                with gr.Column():
                    gr.Markdown("# Status")
                    EPP_status_textbox = gr.Textbox(label="Status",value="Solved",interactive=False)

            # State space tree
            with gr.Row():
                with gr.Column():
                    gr.Markdown("# Solution")
                    EPP_solution_textbox = gr.Textbox(label="Solution",value="",interactive=False)
            
            # Statistics
            # Including: solving time, number of nodes expanded, number of nodes generated, max depth reached
            with gr.Row():
                with gr.Column():
                    gr.Markdown("# Statistics")
                    
                    # solving time
                    gr.Markdown("## Solving Time")
                    EPP_solving_time_textbox = gr.Textbox(label="Solving Time",value="0",interactive=False)

                    # number of nodes expanded
                    gr.Markdown("## Number of Nodes Expanded")
                    EPP_number_of_nodes_expanded_textbox = gr.Textbox(label="Number of Nodes Expanded",value="0",interactive=False)

                    # number of nodes generated
                    gr.Markdown("## Number of Nodes Generated")
                    EPP_number_of_nodes_generated_textbox = gr.Textbox(label="Number of Nodes Generated",value="0",interactive=False)

                    # max depth reached
                    gr.Markdown("## Max Depth Reached")
                    EPP_max_depth_reached_textbox = gr.Textbox(label="Max Depth Reached",value="0",interactive=False)

    # Methods
    EPP_input_parameter_list = [EPP_input_sequence_textbox,EPP_target_sequence_textbox,EPP_algorithm_dropdown,EPP_max_step_textbox]
    EPP_output_parameter_list = [EPP_status_textbox,EPP_solution_textbox,EPP_solving_time_textbox,EPP_number_of_nodes_expanded_textbox,EPP_number_of_nodes_generated_textbox,EPP_max_depth_reached_textbox]
    EPP_submit_button.click(fn=eight_puzzle_problem.EPP_solve,inputs=EPP_input_parameter_list,outputs=EPP_output_parameter_list)

    

with gr.Blocks() as server:

    with gr.Tab("Subjective Bayesian Analysis"):
        create_SBA_interface()
    
    with gr.Tab("8 Puzzle Problem"):
        create_EPP_interface()
    
    with gr.Tab("Help"):
        gr.Markdown("# Help")
        gr.Markdown("This project is build with gradio by Ruhao Tian.")

server.queue().launch(share=False,server_name="0.0.0.0")

