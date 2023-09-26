import matplotlib.pyplot as plt
from . import shared

def clear_SBA_parameter():
    shared.SBA_P_H_not_E = 0.5
    shared.SBA_P_H_E = 0.5
    shared.SBA_P_H = 0.5
    shared.SBA_P_E_S = 0.25
    shared.SBA_P_E = 0.5
    shared.SBA_P_H_S = 0.5
    return [
        shared.SBA_P_H_not_E,
        shared.SBA_P_H_E,
        shared.SBA_P_H,
        shared.SBA_P_E_S,
        shared.SBA_P_E,
        shared.SBA_P_H_S,
    ]

def SBA_plot_and_calculate(
        SBA_P_H_not_E,
        SBA_P_H_E,
        SBA_P_H,
        SBA_P_E_S,
        SBA_P_E,
        SBA_P_H_S,
):
    # MUST convert input arguments to float type
    # or the xlim function will not work
    # neither will calculations related to the input arguments be correct
    # convert input arguments to float type
    args = [float(arg) for arg in [SBA_P_H_not_E, SBA_P_H_E, SBA_P_H, SBA_P_E_S, SBA_P_E]]

    # unpack the converted arguments
    SBA_P_H_not_E, SBA_P_H_E, SBA_P_H, SBA_P_E_S, SBA_P_E = args

    # calculate the probability of hypothesis given subject
    if SBA_P_E_S >= 0 and SBA_P_E_S <= SBA_P_E:
        SBA_P_H_S = SBA_P_H_not_E + (SBA_P_H - SBA_P_H_not_E) * SBA_P_E_S / SBA_P_E
    elif SBA_P_E_S > SBA_P_E and SBA_P_E_S <= 1:
        SBA_P_H_S = SBA_P_H + (SBA_P_H_E - SBA_P_H) * (SBA_P_E_S - SBA_P_E) / (1 - SBA_P_E)
    else:
        # throw an error
        raise ValueError("P(E|S) must be between 0 and 1")
    
    # document the result
    SBA_P_H_S_raw = SBA_P_H_S
    # truncate the result to 2 decimal places for display
    SBA_P_H_S = round(SBA_P_H_S,2)

    # initialize the plot
    fig = plt.figure(layout="constrained")
    # set the plot title
    # plt.suptitle("Subjective Bayesian Analysis")
    # set the limit of x-axis and y-axis to (0,1)
    plt.xlim(left=0,right=1.0)
    plt.ylim(bottom=0,top=1.0)
    # set the label of x-axis and y-axis
    plt.xlabel("P(E|S)")
    plt.ylabel("P(H|S)")

    # start plotting
    # plot the line start from (0,SBA_P_H_not_E) to (SBA_P_E,SBA_P_H), then to (1,SBA_P_H_E)
    plt.plot([0,SBA_P_E,1],[SBA_P_H_not_E,SBA_P_H,SBA_P_H_E],label="P(H|E) - P(E|S)")
    # mark the point (0, SBA_P_H_not_E), (SBA_P_E,SBA_P_H), (1,SBA_P_H_E), and (SBA_P_E_S,SBA_P_H_S)
    plt.plot(0,SBA_P_H_not_E,marker="o",color="red")
    plt.plot(SBA_P_E,SBA_P_H,marker="o",color="red")
    plt.plot(1,SBA_P_H_E,marker="o",color="red")
    plt.plot(SBA_P_E_S,SBA_P_H_S,marker="o",color="green")
    # add dashed lines connecting the marked points and their projections on the x-axis and y-axis
    # point (0, SBA_P_H_not_E)
    plt.plot([0,0],[SBA_P_H_not_E,SBA_P_H_not_E],linestyle="--",color="gray")
    plt.plot([0,0],[SBA_P_H_not_E,0],linestyle="--",color="gray")
    # point (SBA_P_E,SBA_P_H)
    plt.plot([SBA_P_E,SBA_P_E],[0,SBA_P_H],linestyle="--",color="gray")
    plt.plot([SBA_P_E,0],[SBA_P_H,SBA_P_H],linestyle="--",color="gray")
    # point (1,SBA_P_H_E)
    plt.plot([1,1],[0,SBA_P_H_E],linestyle="--",color="gray")
    plt.plot([1,0],[SBA_P_H_E,SBA_P_H_E],linestyle="--",color="gray")
    # point (SBA_P_E_S,SBA_P_H_S)
    plt.plot([SBA_P_E_S,SBA_P_E_S],[0,SBA_P_H_S],linestyle="--",color="gray")
    plt.plot([SBA_P_E_S,0],[SBA_P_H_S,SBA_P_H_S],linestyle="--",color="gray")
    
    # generating the xticks and yticks corresponding to the marked points
    SBA_P_H_not_E_ytick = "P(H|NE)\n"+(str)(SBA_P_H_not_E)
    SBA_P_H_ytick = "P(H)\n"+(str)(SBA_P_H)
    SBA_P_H_E_ytick = "P(H|E)\n"+(str)(SBA_P_H_E)
    SBA_P_H_S_ytick = "P(H|S)\n"+(str)(SBA_P_H_S)

    SBA_P_E_xtick = "P(E)\n" + (str)(SBA_P_E)
    SBA_P_E_S_xtick = "P(E|S)" + (str)(SBA_P_E_S)
    # add the xticks and yticks
    plt.xticks([0,1,SBA_P_E,SBA_P_E_S],["0","1",SBA_P_E_xtick,SBA_P_E_S_xtick])
    plt.yticks([SBA_P_H_not_E,SBA_P_H,SBA_P_H_E,SBA_P_H_S],[SBA_P_H_not_E_ytick,SBA_P_H_ytick,SBA_P_H_E_ytick,SBA_P_H_S_ytick])

    return fig,(float)(SBA_P_H_S_raw)

    
    