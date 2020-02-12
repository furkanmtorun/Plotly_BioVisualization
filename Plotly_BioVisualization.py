# Plotly BioVisualization with Python by @furkanmtorun 
# |-> [furkanmtorun@gmail.com](mailto:furkanmtorun@gmail.com) 
# |-> GitHub: [@furkanmtorun](https://github.com/furkanmtorun)  
# |-> [Google Scholar](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ) 
# |-> [Personal Website](https://furkanmtorun.github.io/)

import json
import dash
import math as m
import pandas as pd
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html

# Set the CSS files for customizing the appearance of the page and components.
# Here, I prefer to use Bulma.css as a CSS framework.
external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css"]

# Set the app configuration
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Import TP53 Variation and Domain Data
with open('TP53.json', "r") as variant_domain_json_data:
    mutationData = json.load(variant_domain_json_data)

# Import TP53 MSA Data
alignment_data = open('fasta.txt', "r",  encoding="utf-8").read()

# Import GWAS Data for Manhattan Plot
gwas_data = pd.read_csv('gwas_data.csv')

# Page Layout Begins
app.layout = html.Div(id="fmt_envelope", children=[
    html.Div(className="hero is-light is-medium hero-body columns is-centered is-12 has-text-centered", children=[
        html.Img(src="https://avatars0.githubusercontent.com/u/49681382?s=180", style={"height": 180, "width": 180, "borderRadius": "50%", "margin": "10px auto"}),
        html.H1("Plotly BioVisualization", id="header_title", className="title"),
        html.Div("with Python by @furkanmtorun", className="subtitle"),
        html.Div(children=[
            html.A("Mail", href="mailto:furkanmtorun@gmail.com", className="button is-link is-outlined is-medium"),
            html.A("GitHub", href="https://github.com/furkanmtorun", target="_blank", className="button is-dark is-outlined is-medium", style={"marginLeft": 5}),
            html.A("Scholar", href="https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ", target="_blank", className="button is-primary is-outlined is-medium",  style={"marginLeft": 5}),
            html.A("Twitter", href="https://twitter.com/furkanmtorun", target="_blank", className="button is-info is-outlined is-medium", style={"marginLeft": 5}),
            html.A("Web", href="https://furkanmtorun.github.io/", target="_blank", className="button is-danger is-outlined is-medium", style={"marginLeft": 5}),
        ]),
            html.A("Check here out now for installation and usage!", target="_blank", href="http://github.com/furkanmtorun/Plotly_BioVisualization", className="button is-warning rounded", 
                    style={"margin": "10px auto", "padding": 20, "width": 450, "fontWeight":"bold", "textAlign":"center"}),
    ]),
    
    # Needle Plot Component
    html.Div(className="columns is-centered is-vcentered has-background-info", style={"padding": "40px 25px 50px 55px"},
        children=[
            html.Div(className="column is-half is-primary is-centered", children=[
                html.H1("Needle Plot for Proteins", className="title has-text-white-bis"),
                html.P("It allows you to illustrate the mutations or other changes on the corresponding positions of amino acids within the protein sequence together with the protein domains.", 
                        className="subtitle is-5 has-text-white-bis"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-light is-rounded"),
                html.Hr(),
                html.H1("Data Structure for Needle Plot", className="title has-text-white-bis"),
                html.P("Here is the structure of the JSON file containing the variants and the domains. In this example, TP53 protein variants and domains were given.", className="subtitle is-5 has-text-white-bis"),
                html.Div("{ x: [], y: [], domains: [], mutationGroups: [] }", className="notification is-light"),
                html.A("+ Please click here to visit my another repository if you would like to get gnomAD variants!", href="https://github.com/furkanmtorun/gnomad_python_api", target="_blank", className="has-text-warning"),
            ]),
            html.Div(className="column is-half is-primary is-centered", children=[
                
                # Here is the needle plot!  
                dashbio.NeedlePlot(
                    id = "fmt_needle_plot",
                    mutationData = mutationData, 
                    needleStyle = {
                        "headSize": 10,
                        "stemThickness": 3,
                        "stemColor": "#CCC",
                        "stemConstHeight": False, # If you would like to make all needle in same height, turn it into True.
                        "headSymbol": ["circle", "square", "triangle-up", "diamond"], # If you would like to make them same, remove this line.
                        # "headColor": ["blue", "purple"] # If you would like to change color of needle heads, work on here.
                    },
                    domainStyle = {
                        "displayMinorDomains": True, # If you would like to neglect the minor domains, stay it as True.
                    },
                    rangeSlider = False, # If you would like to enable range slider (for enabling to filter based on position), turn it into True.
                    xlabel = "Sequence of the protein",
                    ylabel = "# of Mutations",
                ), # ends of needle plot

            ]),
        ] # ends of 'columns'
    ),

    # Sequence Viewer Component
    #https://dash.plot.ly/dash-bio/alignmentchart
    html.Div(className="columns is-centered is-vcentered has-background-primary", style={"paddingLeft": 55},
        children=[
            html.Div(className="column is-three-fifths is-centered", children=[
                
                # Here is alignment chart!
                dashbio.AlignmentChart(
                    id = "fmt_alignment_viewer",
                    data = alignment_data,
                    extension = "fasta", # If your data contains clustal output, turn it into "clustal".
                    colorscale =  "clustal2", # If yo would like to change the color schema, work on here.
                    showgap = False,
                    showconsensus = True, # If you would like to just enable alignment part, turn it into False.
                    showconservation = True, # If you would like to just enable alignment part, turn it into False.
                    tilewidth = 20, # It defines the width of the each amino acid/nucleotid box.
                    tileheight = 20, # It defines the height of the each amino acid/nucleotid box.
                    showid = False,
                    overview = "slider", # If you would like to change, turn it into "heatmap" or "none" for disabling.
                    height = 490,
                    width = "95%",
                ), # ends of alignment chart
                
            ]),
            html.Div(className="column is-centered", style={"padding": "30px 55px 30px 0px"}, children=[
                html.H1("Sequence Alignment Viewer", className="title has-text-white-bis"),
                html.P("It allows you to visualize the genomics and transcriptomic sequence with several features such as coverage, gaps, consensus and heatmap overview.", 
                        className="subtitle is-5 has-text-white-bis"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-light is-rounded"),
                html.Hr(),
                html.P("*FASTA or Clustal formats can be used here.", className="subtitle is-6 has-text-white-bis"), 
                html.P("*Some options are altered/disabled in this example. Just look at the code and comments!", className="subtitle is-6 has-text-white-bis"), 
            ]),
        ]), # ends of Sequence Viewer

    # Manhattan Plot Component
    html.Div(className="columns is-centered is-vcentered", style={"paddingLeft": 55, "paddingRight": 25},
        children=[
            html.Div(className="column is-half is-centered", children=[
                html.H1("Manhattan Plot", className="title"),
                html.P("Manhattan Plot is a type of scatter plot and commonly used in genome-wide association studies (GWAS) to visualize display significant SNPs efficiently.", 
                        className="subtitle is-5"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-info is-rounded"),
                html.Hr(style={"background": "#CCC"}),
                html.P("*The genome-wide significance threshold was set as 5e-8 and plotted with green line, and the most significant SNPs are colored in red.", className="subtitle is-5"), 
            ]),
            html.Div(className="column is-half is-centered", children=[
                
                # Here is Manhattan Plot 
                dcc.Graph(figure=dashbio.ManhattanPlot(
                    dataframe = gwas_data,
                    highlight_color = "#ff3860",
                    genomewideline_value = -(m.log10(5e-8)),
                    genomewideline_width = 2, # Boldness of the genome-wide line
                    genomewideline_color = "#00d1b2",
                    suggestiveline_value = False, # If you would like to add a suggestive threshold, turn it into a float value.
                    annotation = "ADD_INFO", # If you would like to add extra info to the annotation part, here put the column name.
                    showgrid = False,
                    title = None,
                    xlabel = "chromosome"
                )), # ends of Manhattan Plot 

            ]),
        ]), 

    # Footer Part
    html.Div(className="columns is-centered is-vcentered has-background-light", style={"padding": "100px 0px"},
        children=[
            html.Div(className="column is-half is-centered is-vcentered", children=[
                html.H1("Thanks for your effort to open and come here!", className="title"),
                html.P("I will keep continue to append new interactive graphs and figures as much as I can.", className="subtitle is-5"),
                html.Br(),
                html.Hr(style={"background": "#CCC"}),
                html.Br(),
                html.H1("Contributing & Feedback", className="title"),
                html.P("I would be very happy to see any feedbacks and contributions on this repository!", className="subtitle is-5"),
                html.A("@furkanmtorun", className="button is-medium"),
                html.A("Mail", href="mailto:furkanmtorun@gmail.com", className="button is-link is-medium", style={"marginLeft": 5}),
                html.A("GitHub", href="https://github.com/furkanmtorun", target="_blank", className="button is-dark is-medium", style={"marginLeft": 5}),
                html.A("Scholar", href="https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ", target="_blank", className="button is-primary is-medium",  style={"marginLeft": 5}),
                html.A("Twitter", href="https://twitter.com/furkanmtorun", target="_blank", className="button is-info is-medium", style={"marginLeft": 5}),
                html.A("Web", href="https://furkanmtorun.github.io/", target="_blank", className="button is-danger is-medium", style={"marginLeft": 5}),
                html.Br()
            ])
        ]), # ends of footer

]) #ends of page layout

if __name__ == "__main__":
    app.run_server(debug=True)