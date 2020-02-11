# Plotly BioVisualization with Python by @furkanmtorun 
# |-> [furkanmtorun@gmail.com](mailto:furkanmtorun@gmail.com) 
# |-> GitHub: [@furkanmtorun](https://github.com/furkanmtorun)  
# |-> [Google Scholar](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ) 
# |-> [Personal Website](https://furkanmtorun.github.io/)

import json
import dash
import dash_bio as dashbio
import dash_core_components as dcc
import dash_html_components as html

# Set the CSS files
external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css"]

# Set the app configuration
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open('TP53.json', "r") as variant_domain_json_data:
    mutationData = json.load(variant_domain_json_data)

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
    html.Div(className="columns is-centered is-vcentered", style={"paddingLeft": 55, "paddingRight": 25, "marginBottom": 50},
        children=[
            html.Div(className="column is-half is-primary is-centered", children=[
                html.H1("Needle Plot for Proteins", className="title"),
                html.P("It allows you to illustrate the mutations or other changes on the corresponding positions of amino acids within the protein sequence together with the protein domains.", 
                        className="subtitle is-5"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-success is-rounded"),
                html.Hr(),
                html.H1("Data Structure for Needle Plot", className="title"),
                html.P("Here is the structure of the JSON file containing the variants and the domains. In this example, TP53 protein variants and domains were given.", className="subtitle is-5"),
                html.Div("{ x: [], y: [], domains: [], mutationGroups: [] }", className="notification is-light"),
                html.A("*Please, visit my another repository if you would like to illustrate the gnomAD variants. Click here!", href="https://github.com/furkanmtorun/gnomad_python_api", target="_blank"),
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
                    rangeSlider = False, # If you would like to enable range slider (filtering based on position), turn it into True 
                    xlabel = "Sequence of the protein",
                    ylabel = "# of Mutations",
                ), 
                # ends of needle plot
            ]),
        ] # ends of columns div
    ),

    # Another Plot Component
    html.Div(className="columns is-centered is-vcentered has-background-primary", style={"paddingLeft": 55, "paddingRight": 25},
        children=[
            html.Div(className="column is-half is-centered", children=[
                # Here is another plot!
                dcc.Graph(
                    id="another_plot_1",
                    figure={
                        "data": [
                            {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "PlotLegend1"},
                            {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "PlotLegend2"},
                        ],
                        "layout": { "title": "Another Plot #1" }
                    }
                ) # ends of another plot 
            ]),
            html.Div(className="column is-half is-centered", children=[
                html.H1("Another Plot #1", className="title has-text-white-bis"),
                html.P("Another Plot Info #1", 
                        className="subtitle is-5 has-text-white-bis"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-light is-rounded"),
                html.Hr(),
                html.P("Something else.", className="subtitle is-5 has-text-white-bis"), 
            ]),
        ]), # ends of another plot

    # The other Plot Component
    html.Div(className="columns is-centered is-vcentered has-background-info", style={"paddingLeft": 55, "paddingRight": 25},
        children=[
            html.Div(className="column is-half is-centered", children=[
                html.H1("Another Plot #2", className="title has-text-white-bis"),
                html.P("Another Plot Info #2", 
                        className="subtitle is-5 has-text-white-bis"),
                html.A("Go to Docs for 'Dash' library", href="https://dash.plot.ly/", target="_blank", className="button is-outlined is-light is-rounded"),
                html.Hr(),
                html.P("Something else.", className="subtitle is-5 has-text-white-bis"), 
            ]),
            html.Div(className="column is-half is-centered", children=[
                # Here is the other plot!
                dcc.Graph(
                    id="another_plot_2",
                    figure={
                        "data": [
                            {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "PlotLegend1"},
                            {"x": [1, 2, 3], "y": [20, 4, 5], "type": "bar", "name": "PlotLegend2"},
                        ],
                        "layout": { "title": "Another Plot #2" }
                    }
                ) # ends of another plot 
            ]),
        ]), # ends of the other plot

    # Thanks Component
    html.Div(className="columns is-centered is-vcentered has-background-light", style={"padding": "100px 0px"},
        children=[
            html.Div(className="column is-half is-centered is-vcentered", children=[
                html.H1("Thanks for your effort to open and come here!", className="title"),
                html.P("I will keep continue to append new interactive graphs and figures as much as I can.", className="subtitle is-5"),
                html.Hr(style={"background": "#555"}),
                html.H1("Contributing & Feedback", className="title"),
                html.P("I would be very happy to see any feedbacks and contributions on this repository!", className="subtitle is-5"),
                html.A("@furkanmtorun", className="button is-medium"),
                html.A("Mail", href="mailto:furkanmtorun@gmail.com", className="button is-link is-medium", style={"marginLeft": 5}),
                html.A("GitHub", href="https://github.com/furkanmtorun", target="_blank", className="button is-dark is-medium", style={"marginLeft": 5}),
                html.A("Scholar", href="https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ", target="_blank", className="button is-primary is-medium",  style={"marginLeft": 5}),
                html.A("Twitter", href="https://twitter.com/furkanmtorun", target="_blank", className="button is-info is-medium", style={"marginLeft": 5}),
                html.A("Web", href="https://furkanmtorun.github.io/", target="_blank", className="button is-danger is-medium", style={"marginLeft": 5}),
            ])
        ]), # ends of the other plot


]) #ends of page layout

if __name__ == "__main__":
    app.run_server(debug=True)