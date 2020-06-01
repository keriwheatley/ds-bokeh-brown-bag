from bokeh.io import curdoc
from bokeh.layouts import gridplot, WidgetBox
from bokeh.models import Button, ColumnDataSource, Div, MultiSelect, Panel
from bokeh.models.widgets import Tabs
from scripts.load_data import load_data, preprocess_data
from scripts.create_plot import make_plot1, make_plot2

##########
##########    Load data
##########
df = load_data()


##########
##########    Preprocess data
##########
source = preprocess_data(df)


##########
##########    Create checkerbox filter
##########
years_list = sorted(df['CalendarYearIssued'].astype(str).unique().tolist())

year_selection = MultiSelect(title='Year'
                            , value=[str(i) for i,j in enumerate(years_list)]
                            , options = [(str(i),j) for i,j in enumerate(years_list)])


##########
##########    Create select all button
##########
def update_selectall():
    year_selection.value = [x[0] for x in year_selection.options]

select_all = Button(label='Select All')
select_all.on_click(update_selectall)


##########
##########    Create run button
##########
def update_run():
    years_to_plot = [x[1] for x in year_selection.options if x[0] in year_selection.value]
    new_data = df[df['CalendarYearIssued'].isin(years_to_plot)]
    new_source = preprocess_data(new_data)
    source.data.update(new_source.data)

update_plot = Button(label='Update Plot')
update_plot.on_click(update_run)


##########
##########    Create widgets box
##########
controls = WidgetBox(Div(text='<h1>Widgets Box</h1>'), year_selection, select_all, update_plot, width=150)


##########
##########    Create plots
##########
p1 = make_plot1(source)
p2 = make_plot2(source)


##########
##########    Create layout for items
##########
layout1 = gridplot(children=[[controls, p1]])
tab1 = Panel(child=layout1, title = 'Project Values')

layout2 = gridplot(children=[[p2]])
tab2 = Panel(child=layout2, title = 'Project Counts')

tabs = Tabs(tabs = [tab1, tab2])
curdoc().add_root(tabs)