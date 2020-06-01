from bokeh.io import show, output_notebook
from bokeh.models import ColumnDataSource, HoverTool, PointDrawTool, ResetTool, WheelZoomTool
from bokeh.plotting import figure



##########
##########    Add styling
##########
def style(p):

    p.legend.location = "top_left"

    p.plot_height=500
    p.plot_width=800

    p.title.align = 'center'
    p.title.text_font_size = '14pt'

    p.xaxis.axis_label_text_font_size = '12pt'
    p.xaxis.axis_label_text_font_style = 'normal'
    p.xaxis.major_label_text_font_size = '12pt'

    p.yaxis.axis_label_text_font_size = '12pt'
    p.yaxis.axis_label_text_font_style = 'normal'
    p.yaxis.major_label_text_font_size = '12pt'

    p.toolbar_location='above'

    return p



def make_plot1(source):

    ##########
    ##########    Create figure
    ##########

    p = figure(plot_height=400
            , plot_width=700
            , title='Austin Construction Permit Project Valuations'
            )


    ##########
    ##########    Create first glyph with hovertool
    ##########

    # Create line on plot
    total_renderer = p.line(x='CalendarYearIssued'
            , y='TotalInBillions'
            , color='orange'
            , line_width=4
            , source=source
            , legend='Total Valuation All Projects'
        )

    # Define hover functionality
    deftooltips = [
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
        ("Calendar Year Issued", "@CalendarYearIssued"),
        ("Total In Billion $", "@TotalInBillions"),
    ]

    # Create hovertool and add to figure
    total_hover = HoverTool(tooltips=deftooltips, renderers=[total_renderer])
    p.add_tools(total_hover)


    ##########
    ##########    Create second glyph with hovertool
    ##########

    # Create line on plot
    avg_renderer = p.line(x='CalendarYearIssued'
                , y='MaxInBillions'
                , color='green'
                , line_width=4
                , source=source
                , legend='Average Valuation per Project'
        )

    # Define hover functionality
    deftooltips = [
        ("index", "$index"),
        ("(x,y)", "($x, $y)"),
        ("Calendar Year Issued", "@CalendarYearIssued"),
        ("Average in $", "@mean{(0,0)}"),
    ]

    # Create hovertool and add to figure
    avg_hover = HoverTool(tooltips=deftooltips, renderers=[avg_renderer])
    p.add_tools(avg_hover)


    ##########
    ##########    Create third glyph cirles with point-draw functionality
    ##########

    # Create circles on plot
    circles_renderer = p.circle(x='CalendarYearIssued'
                , y='TotalInBillions'
                , fill_color='white'
                , line_color='orange'
                , size=6
                , source=source)

    # Define point draw functionality
    circles_point_draw = PointDrawTool(renderers=[circles_renderer])
    p.add_tools(circles_point_draw)

    # Add labels
    p.xaxis.axis_label = 'Year Permits Issued'
    p.yaxis.axis_label = 'Billion Dollars ($B)'

    # Clean up toolbar
    tools = [avg_hover, total_hover, WheelZoomTool(), ResetTool()]
    p.tools = tools

    # Style chart
    p = style(p)

    return p


def make_plot2(source):
    # Create figure
    p = figure(plot_height=400
            , plot_width=700
            , title='Count of Issued Construction Permits'
            )

    # Creating glyphs
    renderer = p.vbar(x='CalendarYearIssued'
            , top='count'
            , color='purple'
            , width=0.9
            , source=source
        )

    # Add labels
    p.xaxis.axis_label = 'Year Permits Issued'
    p.yaxis.axis_label = 'Number of Permits Issued'

    # Style chart
    p = style(p)

    return p