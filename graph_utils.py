import matplotlib.pyplot as plt
import squarify
import plotly.express as px
import plotly.graph_objects as go
from pywaffle import Waffle
import math
import pandas as pd

global global_color_codes, global_plotly_template

global_color_codes = [
    "#00FFFF", "#F0FFFF", "#89CFF0", "#0000FF", "#7393B3", "#088F8F",
    "#0096FF", "#5F9EA0", "#0047AB", "#6495ED", "#00FFFF", "#00008B",
    "#6F8FAF", "#1434A4", "#7DF9FF", "#6082B6", "#00A36C", "#3F00FF",
    "#5D3FD3", "#ADD8E6", "#191970", "#000080", "#1F51FF", "#A7C7E7",
    "#CCCCFF", "#B6D0E2", "#96DED1", "#4169E1", "#0F52BA", "#9FE2BF",
    "#87CEEB", "#4682B4", "#008080", "#40E0D0", "#0437F2", "#40B5AD", "#0818A8"
]

global_plotly_template = "plotly_dark"


def draw_plotly_bar(dataframe, x_column_name, y_column_name, title, x_axis_title, y_axis_title, show_legend=False):
    colors = global_color_codes
    if len(dataframe) >= len(colors):
        diff = len(dataframe) - len(colors) + 2
        colors = colors + colors[:diff]
    figure = px.bar(dataframe, x=x_column_name, y=y_column_name,
                    color=colors[-len(dataframe):], template=global_plotly_template, title=title)
    figure.update_layout({
        "yaxis": {
            "title": y_axis_title
        },
        "xaxis": {
            "title": x_axis_title
        },
        "showlegend": show_legend
    })

    figure.show()

    return figure


def draw_plotly_pie(dataframe, values_column: str, names_column: str, title: str, hover_info: list, x_axis_title: str, y_axis_title: str, col2labels=None):
    colors = global_color_codes
    if len(dataframe) >= len(colors):
        diff = len(dataframe) - len(colors) + 2
        colors = colors + colors[:diff]
    figure = px.pie(
        dataframe, values=values_column, names=names_column, title=title, hover_data=hover_info, labels=col2labels, template=global_plotly_template
    )
    figure.update_traces(textposition='inside', textinfo='percent+label')
    figure.update_layout(
        {"yaxis": {"title": y_axis_title}, "xaxis": {"title": x_axis_title}})
    figure.show()

    return figure


def draw_treemap(dataframe, count_column, labels_column, label_prefix=None):

    counts = dataframe[count_column].values.tolist()
    labels = [f"{label_prefix if label_prefix else ''} {l}" for l in dataframe[labels_column
                                                                               ].values.tolist()]
    color = global_color_codes[-len(dataframe):]
    plt.figure(figsize=(20, 10))
    squarify.plot(sizes=counts, label=labels, color=color, alpha=.9)
    plt.axis("off")
    plt.show()


def draw_waffle(data_dict, title_label, font_size, face_color, text_color, is_percent=False):
    if not is_percent:
        totals = sum([v for k, v in data_dict.items()])
        data_dict = {k: round(math.ceil((v/totals)*100))
                     for k, v in data_dict.items()}
    fig = plt.figure(FigureClass=Waffle, rows=5, values=data_dict, colors=global_color_codes[:len(data_dict)], title={
        "label": title_label,
        "loc": "left"
    }, legend={"loc": "upper left", "bbox_to_anchor": (1, 1)}, figsize=(20, 10), starting_location="NW", block_arranging_style="snake")

    fig.set_facecolor(face_color)

    plt.rcParams['text.color'] = text_color
    plt.rcParams['font.size'] = font_size

    plt.show()


def draw_donut(dataframe, count_column, names_column, face_color, font_size, text_color, is_percent=False):

    names = dataframe[names_column].values.tolist()
    sizes = dataframe[count_column].values.tolist()
    if is_percent:
        names = [f"{names[ix]} - {sizes[ix]}%" for ix in range(len(names))]
    else:
        names = [
            f"{names[ix]} - {round(math.ceil((sizes[ix]/sum(sizes)) * 100))}%" for ix in range(len(names))]

    fig = plt.figure()
    fig.patch.set_facecolor(face_color)

    plt.rcParams['text.color'] = text_color
    plt.rcParams['font.size'] = font_size

    circle = plt.Circle((0, 0), 1, color=face_color)

    plt.pie(sizes, labels=names, radius=4,
            colors=global_color_codes[len(sizes):])
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.show()


def draw_plotly_stack_chart(data_dict, title):

    graph_df = pd.DataFrame.from_dict(data_dict)
    graph_df["name"] = graph_df.index.tolist()

    figure = px.bar(graph_df, x="name", y=[
                    c for c in graph_df.columns if not c == "name"], template=global_plotly_template, title=title)
    figure.show()

    return figure


def draw_plotly_group_chart(data_dict, title):

    figure = go.Figure(data=[
        go.Bar(name=k, x=list(_v.keys()), y=list(_v.values()))
        for k, _v in data_dict.items()
    ])
    figure.update_layout(
        barmode='group', template=global_plotly_template, title=title)
    figure.show()

    return figure
